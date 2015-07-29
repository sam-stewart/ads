def biggestint(l):
    if len(l) == 1:
        return l[0]
    if (l[0] < l[1]):
        l2 = l[1:]
    else:
        l2 = [l[0]] + l[2:]
    return biggestint(l2)

# Not my code but it's interesting to examine. (Hence all the print statements)
# A good illustration of the nature of the stack I feel.
def biggestint2(l):
    print l
    if len(l) == 1:
        print "hit if statement"
        return l[0]
    else:
        m = biggestint2(l[1:])
        print l
        print "m " + str(m)
        print l[0]
        return m if m > l[0] else l[0]

# Given a string of digits, write a recursive function that returns the corresponding int.
def determineint(s):
    if len(s) == 0:
        return 0
    return int(s[0] + ((len(s)-1) * "0")) + determineint(s[1:])
