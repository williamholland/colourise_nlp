import fileinput
import nltk
import csv


RTF_HEADER = '''\
{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0 \\fswiss LiberationSans;}}
{\\colortbl;\
'''


class TaggingEngine(object):

    def get_tags_colours_mapping(self):
        with open('word_class.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t')
            self.tags_colours_mapping = [(row['TAG'], tuple(map(int, row['COLOUR'].split(',')))) for row in reader]

    def init_rtf(self):
        print RTF_HEADER
        for _, rgb in self.tags_colours_mapping:
            print r'    \red{}\green{}\blue{};'.format(*rgb)
        print '}'
        print '\widowctrl\hyphauto'

    def _get_colour_rtf(self, tag):
        for i, (t, _) in enumerate(self.tags_colours_mapping):
            if t == tag:
                return i + 1
        return 0

    def tag_rtf(self, text):
        tokens = nltk.word_tokenize(text)
        tags = nltk.pos_tag(tokens) # [('test', 'NN')]
        result = ''
        for word, tag in tags:
            colour = self._get_colour_rtf(tag)
            result = result + "{\\cf%s %s }" % (colour, word)
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
            sentence += '\n'
    except KeyboardInterrupt:
        pass
    tagging_engine.eof()


if __name__ == '__main__':
    main()
