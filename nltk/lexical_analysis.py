# coding: 'utf-8'
#Adapted from code examples in S. Bird, E. Klein, and E. Loper.
#Natural language processing with Python. OReilly Media, 2009
#
#Takes a text file and tokenizes it words, converts to lower lase, filters stop words,
#builds vocab for text, calculates lexical diversity, builds collocation, builds frequency
#distribtion of most common words, builds example dispersion plot of words of interest
#(manually entered below in this script), then displays results

import nltk
from nltk.corpus import stopwords
from sys import argv

script, inputfilename = argv #takes whatever filename you pass in

print inputfilename

raw = open("%s" % inputfilename).read() #loads incident descriptions identified as being due to computer problems

tokens = nltk.wordpunct_tokenize(raw) #tokenizes free text

#tokens = [nltk.PorterStemmer().stem(t) for t in tokens]
# uncomment to stem tokens

#tokens = [nltk.WordNetLemmatizer().lemmatize(t) for t in tokens]
# uncomment to lemmatize tokens

text = nltk.Text(tokens) #defines text

words = [w.lower() for w in text] #defines words and makes all words lower case

filtered_words = [w for w in words if not w in stopwords.words('english')] #removes commonly occuring words ("stop words")

vocab = sorted(set(words)) #defines vocabulary

def lexical_diversity(text): #calculate lexical diversity
    return len(text) / len(set(words))

print "the number of words in the text is %d" % len(text)

print "the number of words in the vocabulary is %d" % len(vocab)

print "lexical diversity is %d" % lexical_diversity(text) #prints lexical diversity

print "here are the collocations.... \n"

text.collocations() #builds collocations

#fdist = nltk.FreqDist(filtered_words)

#fdist.plot(50, cumulative=True) #prints a cumulative frequency distribution of the 50 most commonly used words in the text

#text.dispersion_plot(["police", "alcohol", "drunk", "weather", "unexpected", "injury", "rescue"]) #example dispersion plot using arbitary seach terms
