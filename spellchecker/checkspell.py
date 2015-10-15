#!/usr/bin/python

import sys
import spellchecker
import string


def getline():
    """ return a tuple containing a list of words pertaining to a line from a
    file and the line number """
    count = 1
    for line in open(sys.argv[1]):
        yield line.lower().split(), count
        count += 1

if __name__ == "__main__":
    for words, l in getline():
        for w in words:
            w = w.translate(None, string.punctuation)
            checked = spellchecker.check(w)
            if not checked:
                print str(l) + "\t" + w + "\t" + "No corrections"
            elif checked[0] != w:
                print str(l) + "\t" + w + "\t" + str(checked)
