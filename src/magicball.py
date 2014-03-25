import nltk

sent = "What doesn't kill you, only makes you stronger"

tokens = nltk.word_tokenize(sent)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)

print entities 
