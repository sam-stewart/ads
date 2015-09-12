from sparselist2 import SparseList


sl = SparseList(10)
sl[0] = 7
sl[2] = 4
sl[5] = 3

for x in sl:
    print x
