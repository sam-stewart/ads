#!/usr/bin/python
from stack import Stack
import sys
import operator

if len(sys.argv) != 2:
    print "Wrong number of arguments"
    sys.exit(1)

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.div}

chars = sys.argv[1].split()
stack = Stack()

for x in chars:
    if len(stack) == 2:
        stack.push(ops[x](stack.pop(), stack.pop()))
    else:
        stack.push(int(x))

print stack.pop()
