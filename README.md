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
each tag can be configured by changing the `.cfg` file used (see
`default.cfg`). A description of each tag can be found in `word_class.csv`.
The default colours are showin in the table below.


| TAG | DESCRIPTION | COLOUR |
| --- | ----------- | ------ |
| `NOUN` | noun | ![#135cd0](https://placehold.it/15/135cd0/000000?text=+) `#135cd0` |
| `VERB` | verb | ![#2cc631](https://placehold.it/15/2cc631/000000?text=+) `#2cc631` |
| `ADJ` | adjective | ![#9f00bd](https://placehold.it/15/9f00bd/000000?text=+) `#9f00bd` |
| `ADV` | adverb | ![#328a5d](https://placehold.it/15/328a5d/000000?text=+) `#328a5d` |
| `ADP` | preposition and postposition | ![#fa701d](https://placehold.it/15/fa701d/000000?text=+) `#fa701d` |
| `PRON` | pronoun | ![#f8282a](https://placehold.it/15/f8282a/000000?text=+) `#f8282a` |
| `DET` | determiner | ![#33c3c1](https://placehold.it/15/33c3c1/000000?text=+) `#33c3c1` |
| `NUM` | numeral | ![#555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `CONJ` | conjunction | ![#555753](https://placehold.it/15/555753/000000?text=+) `#555753` |
| `PRT` | particle | ![#555753](https://placehold.it/15/555753/000000?text=+) `#555753` |


## TODO

* pluggable tagger
* output tags to stderr for debugging
* styling: bold, italic, underlined
* take rtf input
* configure target tagset, should probably move to "universal" for default
