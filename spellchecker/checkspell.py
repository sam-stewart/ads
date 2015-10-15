#!/usr/bin/python

import sys
import spellchecker
import string

def getwords(line):
    for word in line.split():
        word = word.translate(None, string.punctuation)
        yield(word.strip().lower())

def getline():
    for line in open(sys.argv[1]):
        yield line.strip()

if __name__ == "__main__":
    line = 1
    for l in getline():
        for w in getwords(l):
            checked = spellchecker.check(w)
            if not checked:
                print str(line) + "\t" + w + "\t" +  "No corrections."
            elif checked[0] != w:
                print str(line) + "\t" + w + "\t" + str(checked)
        line += 1
