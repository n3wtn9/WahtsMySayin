import nltk
import random

def getTagTokens():
    text_file = open("tagtokens.dat","r")
    lines = text_file.readlines()
    text_file.close()
    index = 0
    for line in lines:
       lines[index] = line.strip()
       index = index + 1
    return lines

def getTagLibs():
    text_file = open("taglibs.dat","r")
    lines = text_file.readlines()
    text_file.close()
    index = 0
    for line in lines:
        lines[index] = line.strip()
        index = index + 1
    return lines

def shake(): 
    # input
    sent = "What doesn't kill you, only makes you stronger"
    tagTokens = getTagTokens()
    tagLibs = getTagLibs()

    # randomness
    token_index = random.randrange(0, len(tagTokens), 1)
    adlib_index = random.randrange(0, len(tagLibs), 1) 

    tokens = nltk.word_tokenize(tagLibs[adlib_index])
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)

    # valid pos tag replacement
    valid = 'NN'

    replace_index = -1
    index = 0
    for entity in entities:
        if len(entity) ==2 and entity[1] == valid:
            break
        replace_index = replace_index + 1

    print "original tag: " + tagLibs[adlib_index]
    print "token: " + tagTokens[token_index]
    print entities

    if replace_index != -1:
        entities[replace_index + 1] = (tagTokens[token_index], valid)
   
    return ' '.join([w for w, t in entities.leaves()]) 
