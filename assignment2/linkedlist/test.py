import unittest
from linkedlist import LinkedList


class TestLinkedListReversal(unittest.TestCase):

    def setUp(self):
        self.testelements = [5, 3, 6, 7, 8, 10, 6]
        self.expectedrev = [6, 10, 8, 7, 6, 3, 5]
        self.linkedlist = LinkedList()
        for e in self.testelements:
            self.linkedlist.append(e)

    def test_reversal(self):
        self.linkedlist.reverse()
        rev = [x for x in self.linkedlist]
        self.assertItemsEqual(self.expectedrev, rev)

if __name__ == '__main__':
    unittest.main()
