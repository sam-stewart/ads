""" In place, iterative quicksort module for sorting a python list """
# a, b = left, right

def _swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def _partition(l, a, b):
    # Select last element as pivot
    pivot = l[b]
    left = a
    right = b - 1
    while left <= right:
        while left <= right and l[left] < pivot:
            left += 1
        while left <= right and pivot < l[right]:
            right -= 1
        if left <= right:
            _swap(l, left, right)
            left, right = left + 1, right - 1
    _swap(l, left, b)
    return right

def sort(l):
    """ Sort a given python list of integers with a iterative, in place quick
    sort """
    stack = []
    stack.append((0, len(l) - 1))

    while stack:
        p = stack.pop()
        left, right = p[0], p[1]
        pivot = _partition(l, left, right)
        if pivot - 1 > left:
            stack.append((left, pivot - 1))
        if pivot + 1 < right:
            stack.append((pivot + 1, right))
