import unittest
from linkedbinarytree import LinkedBinaryTree


class TestBreadthFirst(unittest.TestCase):

    def setUp(self):
        """     10
           8          12
        3     9    11     14 """
        self.tree = LinkedBinaryTree()
        p = self.tree._add_root(10)
        p = self.tree._add_left(p, 8)
        self.tree._add_left(p, 3)
        self.tree._add_right(p, 9)

        p = self.tree._add_right(self.tree.root(), 12)
        self.tree._add_left(p, 11)
        self.tree._add_right(p, 14)

    def test_breadthfirst(self):
        expected = [10, 8, 12, 3, 9, 11, 14]
        actual = [x.element() for x in self.tree.breadthfirst()]
        self.assertItemsEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
