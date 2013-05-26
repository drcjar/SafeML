import nltk
from nltk.collocations import *
from nltk.probability import *
from nltk import word_tokenize
from collections import defaultdict
from sys import argv

script, inputfilename = argv

text=open('%s' % inputfilename).read()
words = word_tokenize(text)
   
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = TrigramCollocationFinder.from_words(words)
finder.apply_freq_filter(2)
    
print finder.nbest(trigram_measures.pmi, 50)
