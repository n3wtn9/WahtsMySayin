import random

import nltk


def get_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def shake():
    # input
    tag_tokens = get_lines('tagtokens.dat')
    tag_libs = get_lines('taglibs.dat')

    og_tagline = random.choice(tag_libs)

    tokens = nltk.word_tokenize(og_tagline.lower())
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)

    print "original tagline: " + og_tagline
    return "new tagline:" + ' '.join([w if t != 'NN' else random.choice(tag_tokens) for w, t in entities.leaves()])


if __name__ == '__main__':
    print shake()