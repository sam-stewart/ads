import string
dictionary = set(line.strip() for line in open('words'))

def check(s):
    if s in dictionary:
        return [s]
    possibles = set(transpose(s) + extrachar(s) + missingchar(s) +
                    delchar(s) + replace(s))
    return list(dictionary.intersection(possibles))

def transpose(s):
    """ Return a list of all adjacent character transpositions of s """
    return [s[:i] + s[i+1] + s[i] + s[i+2:] for i in range(len(s) - 1)]

def extrachar(s):
    """ Return a list of all possible strings with a character injected
    between two adjacent characters """
    return [s[:i+1] + c + s[i+1:] for i in range(len(s) - 1) for c in string.ascii_lowercase]

def missingchar(s):
    """ Return a list of all possible strings assuming user missed a single character """
    return [s[:i] + c + s[i:] for i in range(len(s) + 1) for c in string.ascii_lowercase]

def delchar(s):
    """ Return a list of possible strings with a single character deleted from
    the original word """
    return [s[:i] + s[i+1:] for i in range(len(s))]

def replace(s):
    """ Return a list of all possible strings resulting from replacing a
    single character with another one """
    return [s[:i] + c + s[i+1:] for i in range(len(s)) for c in string.ascii_lowercase]
