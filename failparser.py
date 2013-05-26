# coding: 'utf-8'
import nltk
import sys

"""
NHS hackday
Script to clean the html codes out of input files
Each file is converted to a string in the output file.

Usage:
  step 1:  collect filenames in a file using ls > temp.file
  step 2:  $ python failparser.py filenames > output.txt

"""

def main():
  data_names = open(sys.argv[1])
  aname = data_names.readlines()
  for f in aname:
    raw = open(f.strip(), "rb")

    clean = nltk.clean_html(raw.read())

    print clean
    print f, clean, f
    break

if __name__ == '__main__':
    main()
