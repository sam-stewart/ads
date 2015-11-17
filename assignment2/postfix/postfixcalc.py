#!/usr/bin/python
from stack import Stack
import sys
import operator


def calc(chars):
    ops = {'+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div}

    stack = Stack()

    for x in chars:
        if len(stack) == 2:
            stack.push(ops[x](stack.pop(), stack.pop()))
        else:
            stack.push(int(x))
    return stack.pop()

def main():
    if len(sys.argv) != 2:
        print "Wrong number of arguments"
        sys.exit(1)
    print calc(sys.argv[1].split())

if __name__ == '__main__':
    main()
