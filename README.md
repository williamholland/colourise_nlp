# Colourise NLP

Take an input stream of English text and output formatted with colour assigned
to each word according to the tags assigned by `nltk`

![Screenshot.png](https://github.com/williamholland/colourise_nlp/blob/master/img/Screenshot.png)

## Usage

    python colourise_nlp.py < input.txt > output.rtf

## Requires

    * nltk

## Colour Meanings

The colours of each word comes from a tag assigned by `nltk`. The colour of
each tag can be configured in `word_class.csv`. The colour comes from the comma
separated list of red,green,blue values in the COLOUR column. The default
colours as shown in the table below.


| TAG | DESCRIPTION | COLOUR |
| --- | ----------- | ------ |
| `CC` | coordinating conjunction | ![##555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `CD` | cardinal digit | ![##555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `DT` | determiner | ![##33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `EX` | existential there | ![##33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `FW` | foreign word | ![##555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `IN` | preposition/subordinating conjunction | ![##fa701d](https://placehold.it/15/fa701d/000000?text=+) `#fa701d` |
| `JJ` | adjective (large) | ![##9f00bd](https://placehold.it/15/9f00bd/000000?text=+) `#9f00bd` |
| `JJR` | adjective, comparative (larger) | ![##9f00bd](https://placehold.it/15/9f00bd/000000?text=+) `#9f00bd` |
| `JJS` | adjective, superlative (largest) | ![##9f00bd](https://placehold.it/15/9f00bd/000000?text=+) `#9f00bd` |
| `LS` | list market | ![##555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `MD` | modal (could, will) | ![##328a5d](https://placehold.it/15/328a5d/000000?text=+) `#328a5d` |
| `NN` | noun, singular (cat, tree) | ![##135cd0](https://placehold.it/15/135cd0/000000?text=+) `#135cd0` |
| `NNS` | noun plural (desks) | ![##135cd0](https://placehold.it/15/135cd0/000000?text=+) `#135cd0` |
| `NNP` | proper noun, singular (sarah) | ![##135cd0](https://placehold.it/15/135cd0/000000?text=+) `#135cd0` |
| `NNPS` | proper noun, plural (indians or americans) | ![##135cd0](https://placehold.it/15/135cd0/000000?text=+) `#135cd0` |
| `PDT` | predeterminer (all, both, half) | ![##f8282a](https://placehold.it/15/f8282a/000000?text=+) `#f8282a` |
| `POS` | possessive ending (parent's) | ![##33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `PRP` | personal pronoun (hers, herself, him,himself) | ![##33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `PRP$` | possessive pronoun (her, his, mine, my, our ) | ![##33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `RB` | adverb (occasionally, swiftly) | ![##328a5d](https://placehold.it/15/328a5d/000000?text=+) `#328a5d` |
| `RBR` | adverb, comparative (greater) | ![##328a5d](https://placehold.it/15/328a5d/000000?text=+) `#328a5d` |
| `RBS` | adverb, superlative (biggest) | ![##328a5d](https://placehold.it/15/328a5d/000000?text=+) `#328a5d` |
| `RP` | particle (about) | ![##555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `TO` | infinite marker (to) | ![##2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `UH` | interjection (goodbye) | ![##555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `VB` | verb (ask) | ![##2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `VBG` | verb gerund (judging) | ![##2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `VBD` | verb past tense (pleaded) | ![##2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `VBN` | verb past participle (reunified) | ![##2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `VBP` | verb, present tense not 3rd person singular(wrap) | ![##2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `VBZ` | verb, present tense with 3rd person singular (bases) | ![##2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `WDT` | wh-determiner (that, what) | ![##33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `WP` | wh- pronoun (who) | ![##33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `WRB` | wh- adverb (how)  | ![##328a5d](https://placehold.it/15/328a5d/000000?text=+) `#328a5d` |


## TODO

* pluggable tagger
* output tags to stderr for debugging
* styling: bold, italic, underlined
* take rtf input
