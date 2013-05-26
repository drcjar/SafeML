import nltk
from nltk.collocations import *
from nltk.probability import *
from nltk import word_tokenize
from collections import defaultdict
from sys import argv

script, inputfilename = argv

text=open('%s' % inputfilename).read()
words = word_tokenize(text)
 
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(words)
finder.apply_freq_filter(3)
  
print finder.nbest(bigram_measures.pmi, 50)
