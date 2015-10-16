import sys
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


def main():
    parser = argparse.ArgumentParser(description="Spellcheck a given text \
                                     file against a given dictionary file")
    parser.add_argument('-f', '--file', type=file, dest='file',
                        help='file on which to run a spellcheck')
    parser.add_argument('-d', '--dictionary', type=file, dest='dictionary',
                        help='file containing correctly spelled words, each \
                        defined on a new line')
    args = parser.parse_args()

    checker = SpellChecker(args.dictionary)

    for words, l in getline(args.file):
        for w in words:
            w = w.translate(None, string.punctuation)
            checked = checker.check(w)
            if not checked:
                print str(l) + "\t" + w + "\t" + "No corrections"
            elif checked[0] != w:
                print str(l) + "\t" + w + "\t" + str(checked)


if __name__ == "__main__":
    main()
