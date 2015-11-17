#!/usr/bin/python
import argparse
import string
from collections import deque

def wordladder(base, target, dictionary):
    """ Accepts a base word, target word and a valid lexicon. Attempts to
    create a word ladder between the base and target word. Returns the ladder,
    or none """

    used = {base}
    q = deque()
    # Queue first ladder (only base word)
    q.append([base])

    while q:
        # Dequeue ladder at front of queue
        ladder = q.popleft()
        # Get last word on ladder stack
        word = ladder[len(ladder) - 1]
        if word == target:
            return ladder
        # Build all possible words one character different. If it's in
        # the lexicon, and not used, copy old ladder, add new word and add
        # to the queue
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                new = word[:i] + c + word[i+1:]
                if new in dictionary and new not in used:
                    used.add(new)
                    new_ladder = list(ladder)
                    new_ladder.append(new)
                    q.append(new_ladder)
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple program to compute" +
                                     " a word ladder between two words, using" +
                                     " a supplied dictionary")
    parser.add_argument('-b', dest='base', required=True,
                        metavar='<word>',
                        help='word to start the ladder')
    parser.add_argument('-t', dest='target', required=True,
                        metavar='<word>',
                        help='target word')
    parser.add_argument('-d', dest='dictionary', required=True,
                        type=file, metavar='<dictionary file>',
                        help='lexicon file')
    args = parser.parse_args()

    dictionary = {
        line.strip().lower().translate(None, string.punctuation)
        for line in args.dictionary}

    print wordladder(args.base, args.target, dictionary)
