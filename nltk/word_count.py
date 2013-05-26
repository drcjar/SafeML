import nltk
from nltk import word_tokenize
import operator
from collections import defaultdict
from sys import argv

script, inputfilename = argv

print inputfilename

text = open('%s' % inputfilename).read()
words = word_tokenize(text)
  
# improvement due to patch by Paul Masurel
frequencies = defaultdict(int)
   
for w in words:
    frequencies[w] += 1
            
# sort the list before printing
for word, freq in sorted(frequencies.iteritems(), key=operator.itemgetter(1)):
    print str(freq) + "," + word
