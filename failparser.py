import nltk 

raw = open("data/fail/2010FAI10.html", "rb")

clean = nltk.clean_html(raw.read())

print clean
