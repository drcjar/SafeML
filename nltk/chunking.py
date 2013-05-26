#chunks text from file into a noun phrases and prints and draws the result for one sentence 

import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.tag import pos_tag
from sys import argv

script, inputfilename = argv

raw = open('%s' % inputfilename).read()

sentences = sent_tokenize(raw)

print sentences[1]

tagged = pos_tag(word_tokenize(sentences[1]))

patterns = """
NP:  {<DT|PP\$>?<JJ>*<NN>}

"""


NPChunker = nltk.RegexpParser(patterns)

result = NPChunker.parse(tagged)

print result

result.draw()

#wordsenttoke = [word_tokenize(t) for t in sent_tokenize(raw)

#chunks = nltk.tag.batch_pos_tag(sentences)

