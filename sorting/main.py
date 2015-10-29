#!/usr/bin/python
from timeit import timeit
import random


def get_list():
    """ Return an almost sorted list of 500 integers """
    l = range(500)
    # Swap 5 integers
    for i in range(5):
        x = random.randint(0, len(l) -1)
        y = random.randint(0, len(l) -1)
        l[x], l[y] = l[y], l[x]
    return l


if __name__ == "__main__":
    print 'Each sort is run 500 times on a list of 500 integers'

    print 'Quick Sort Random: ' + str(timeit('inplace_quick_sort(l, 0, to)',
        setup='from quick_inplace import inplace_quick_sort;' +
            'import random;' +
            'l = random.sample(range(100000), 500);' +
            'to = len(l) - 1',
            number=500))

    print 'Quick Sort Partial: ' + str(timeit('inplace_quick_sort(l, 0, to)',
        setup='from quick_inplace import inplace_quick_sort;' +
            'from __main__ import get_list;' +
            'l = get_list();' +
            'to = len(l) - 1',
            number=500))

    print 'Merge Sort Random: ' + str(timeit('merge_sort(l)',
        setup='from merge_array import merge_sort;' +
            'import random;' +
            'l = random.sample(range(100000), 500);',
            number=500))

    print 'Merge Sort Partial: ' + str(timeit('merge_sort(l)',
        setup='from merge_array import merge_sort;' +
            'from __main__ import get_list;' +
            'l = get_list();',
            number=500))
