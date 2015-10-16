#!/usr/bin/python
import argparse
from spellchecker import SpellChecker
import string


def getline(f):
    """ return a tuple containing a list of words pertaining to a line from a
    file and the line number """
    count = 1
    for line in f:
        yield line.lower().split(), count
        count += 1


def main(f, dictionary):
    checker = SpellChecker(dictionary)
    for words, l in getline(f):
        for w in words:
            w = w.translate(None, string.punctuation)
            checked = checker.check(w)
            if not checked:
                print str(l) + "\t" + w + "\t" + "No corrections"
            elif checked[0] != w:
                print str(l) + "\t" + w + "\t" + str(checked)
    print str(checker.cache)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spellcheck a given text \
                                     file against a given dictionary file")
    parser.add_argument('-f', type=file, dest='file', required=True,
                        metavar='<test file>',
                        help='file on which to run a spellcheck')
    parser.add_argument('-d', type=file, dest='dictionary', required=True,
                        metavar='<dictionary file>',
                        help='file containing correctly spelled words')
    args = parser.parse_args()

    main(args.file, args.dictionary)
