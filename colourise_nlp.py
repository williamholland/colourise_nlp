import fileinput
import ConfigParser
import sys
import re

import nltk


RTF_HEADER = '''\
{{\\rtf1\\ansi\\deff0{{\\fonttbl{{\\f0 \\fswiss {font};}}}}\
'''


class ColourisedWord(object):

    def __init__(self, tagged_word, tag, whitespace, colour):
        self.tagged_word = tagged_word
        self.tag = tag
        self.whitespace = whitespace
        self.colour = colour

    @property
    def chars(self):
        return self.tagged_word + self.whitespace


def hex_to_rgb( hexi ):
    hex_pattern = '#'+'([a-fA-F0-9]{2})'*3
    rgbs = list(re.match(hex_pattern, hexi).groups())
    return tuple(map(lambda x: int(x, 16), rgbs))


class TaggingEngine(object):

    cfg = 'default.cfg'
    cfg_section = 'Colourise NLP'

    def get_tags_colours_mapping(self):
        ''' () -> list of pairs (<tag str>, <colour tuple of int>)
            read from cfg all the fields starts with tag. then parse as hex
            colours
        '''
        all_items = self.config.items(self.cfg_section)
        tag_items = [o for o in all_items if o[0].startswith('tag.')]
        tag_colours = [hex_to_rgb(o[1]) for o in tag_items]
        tags = [re.sub('^tag\.', '', o[0]).upper() for o in tag_items]
        self.tags_colours_mapping = zip(tags, tag_colours)

    def init_rtf(self):
        print RTF_HEADER.format(font=self.config.get(self.cfg_section, 'font'))
        self._rtf_colours = list(set(t[1] for t in self.tags_colours_mapping))
        sys.stdout.write(r'{\colortbl;')
        for rgb in self._rtf_colours:
            sys.stdout.write(r'\red{}\green{}\blue{};'.format(*rgb))
        print '}'
        print '\widowctrl\hyphauto'

    def _get_colour_from_tag(self, tag):
        for i, (t, c) in enumerate(self.tags_colours_mapping):
            if t == tag:
                return c
        return 0

    def _get_colour_rtf(self, colour):
        for i, c in enumerate(self._rtf_colours):
            if c == colour:
                return i + 1
        return 0

    def tag_python(self, text):
        tokens = nltk.word_tokenize(text)
        tags = nltk.pos_tag(tokens) # gives list like [('test', 'NN')]

        # leading whitespace
        match = re.match('^(\s*)', text)
        if match:
            whitespace = match.groups()[0]
            colour = self._get_colour_from_tag('DEFAULT')
            yield ColourisedWord('', 'DEFAULT', whitespace, colour)

        # tokenize removes spaces, we still want to see them on the screen so add
        # to the left
        total = ''
        text = text.lstrip()
        for tagged_word, tag in tags:
            match = re.match(re.escape(total)+re.escape(tagged_word)+'(\s*)', text)
            whitespace = match.groups()[0]
            total = total + tagged_word + whitespace
            colour = self._get_colour_from_tag(tag)
            yield ColourisedWord(tagged_word, tag, whitespace, colour)

    def tag_rtf(self, text):
        result = ''
        for word in self.tag_python(text):
            c_index = self._get_colour_rtf(word.colour)
            chars = word.chars.replace('\n', r'\line')
            result = result + "{\\f0 \\cf%s %s}" % (c_index, chars)
        return result

    def eof_rtf(self):
        print '}'

    def __init__(self, output_format='rtf'):
        self.output_format = output_format
        self.init_fns = {
            'rtf': self.init_rtf,
        }
        self.tag_fns = {
            'rtf': self.tag_rtf,
        }
        self.eof_fns = {
            'rtf': self.eof_rtf,
        }

    def init(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.cfg)
        self.get_tags_colours_mapping()
        self.init_fns[self.output_format]()

    def tag(self, text):
        return self.tag_fns[self.output_format](text)

    def eof(self):
        self.eof_fns[self.output_format]()
        print '}'


def main():
    tagging_engine = TaggingEngine('rtf')
    tagging_engine.init()
    try:
        # collect chars until get punctuation then send to tagging engine
        sentence = ''
        for line in fileinput.input():
            for c in line:
                sentence = sentence + c
                if c in '.?!':
                    print tagging_engine.tag(sentence)
                    sentence = ''
    except KeyboardInterrupt:
        pass
    tagging_engine.eof()


if __name__ == '__main__':
    main()
