import nltk


def tag(text):
    tokens = nltk.word_tokenize(text)
    return nltk.pos_tag(tokens, tagset='universal')
