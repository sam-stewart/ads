#!/usr/bin/python
from stack import Stack
import sys
import operator


def calc(chars):
    """ Take a postfix expression string, eg.) '3 4 + 7 *', evaluate and
    return the result """
    chars = chars.split()
    ops = {'+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div}

    stack = Stack()

    for x in chars:
        if len(stack) == 2:
            right = stack.pop()
            left = stack.pop()
            stack.push(ops[x](left, right))
        else:
            stack.push(int(x))
    return stack.pop()

def main():
    if len(sys.argv) != 2:
        print "Wrong number of arguments"
        sys.exit(1)
    print calc(sys.argv[1])

if __name__ == '__main__':
    main()
