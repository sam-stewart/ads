#!/usr/local/bin/python3

import random
from timeit import timeit


def test_tree(tree):
    keys = random.sample(range(10000), c)
    for k in keys:
        tree[k] = 0
    while tree:
        del tree[keys.pop()]


if __name__ == "__main__":

    print('Testing search tree implementations, each tree is contructed ' +
          'and broken down 1000 times per run.')

    for c in [100, 200, 400, 800]:
        print('**** Total Elements: ' + str(c) + ' ****')

        print("BST: " + str(timeit('test_tree(t)',
            setup='from __main__ import test_tree;' +
            'from binary_search_tree import TreeMap;' +
                't = TreeMap()', number=1000)))
        print("AVL: " + str(timeit('test_tree(t)',
            setup='from __main__ import test_tree;' +
            'from avl_tree import AVLTreeMap;' +
                't = AVLTreeMap()', number=1000)))
        print("Splay: " + str(timeit('test_tree(t)',
            setup='from __main__ import test_tree;' +
            'from splay_tree import SplayTreeMap;' +
                't = SplayTreeMap()', number=1000)))
        print("RedBlack: " + str(timeit('test_tree(t)',
            setup='from __main__ import test_tree;' +
            'from red_black_tree import RedBlackTreeMap;' +
                't = RedBlackTreeMap()', number=1000)))
