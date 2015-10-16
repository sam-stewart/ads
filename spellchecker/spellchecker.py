import string


class SpellChecker(object):
    """ Python spell checker implemented as described in problem 10.55 in
    Algorithms and Structures with python. """

    def __init__(self, dictfile):
        """ Accept a file reference and parse it into a set. Dictionary file
        should define each word on a new line """
        self.dictionary = set(line.strip().lower() for line in dictfile)

    def check(self, s):
        if s in self.dictionary:
            return [s]
        possibles = set(self.transpose(s) + self.extrachar(s) +
                        self. missingchar(s) + self.delchar(s) + self.replace(s))
        #cachedict[s] = {'cwords': possibles, 'count': 0}
        return list(self.dictionary.intersection(possibles))

    def transpose(self, s):
        """ Return a list of all adjacent character transpositions of s """
        return [s[:i] + s[i+1] + s[i] + s[i+2:] for i in range(len(s) - 1)]

    def extrachar(self, s):
        """ Return a list of all possible strings with a character injected
        between two adjacent characters """
        return [s[:i+1] + c + s[i+1:] for i in range(len(s) - 1)
                for c in string.ascii_lowercase]

    def missingchar(self, s):
        """ Return a list of all possible strings assuming user missed a single
        character """
        return [s[:i] + c + s[i:] for i in range(len(s) + 1)
                for c in string.ascii_lowercase]

    def delchar(self, s):
        """ Return a list of possible strings with a single character deleted
        from the original word """
        return [s[:i] + s[i+1:] for i in range(len(s))]

    def replace(self, s):
        """ Return a list of all possible strings resulting from replacing a
        single character with another one """
        return [s[:i] + c + s[i+1:] for i in range(len(s))
                for c in string.ascii_lowercase]
