""" A heap sort module, reverse engineered from HeapPriorityQueue """

def _parent(j):
    return (j-1) // 2

def _left(j):
    return 2 * j + 1

def _right(j):
    return 2 * j + 2

def _has_left(j, size):
    return _left(j) < size

def _has_right(j, size):
    return _right(j) < size

def _swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def _upheap(l, j, size):
    parent = _parent(j)
    if parent < size:
        if j > 0 and l[parent] < l[j]:
            _swap(l, j, parent)
            _upheap(l, parent, size)

def _downheap(l, j, size):
    if _has_left(j, size):
        left = _left(j)
        large_child = left
        if _has_right(j, size):
            right = _right(j)
            if l[right] > l[left]:
                large_child = right
        if l[large_child] > l[j]:
            _swap(l, j, large_child)
            _downheap(l, large_child, size)

def sort(l):
    """ Sort list l in place with heap sort (mutates list) """
    heapsize = 0
    for i in range(len(l)):
        heapsize += 1
        _upheap(l, heapsize - 1, heapsize)

    for i in range(len(l)):
        _swap(l, 0, heapsize -1)
        heapsize -= 1
        _downheap(l, 0, heapsize)
