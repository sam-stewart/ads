import unittest
import quicksort


class TestQuickSort(unittest.TestCase):

    def setUp(self):
        self.expected = [4, 9, 14, 25, 34, 50, 55]
        self.test = [25, 55, 4, 9, 50, 14, 34]

    def test_quicksort(self):
        quicksort.sort(self.test)
        self.assertItemsEqual(self.test, self.expected)

    def test_empty(self):
        l = []
        self.assertItemsEqual(l, [])

if __name__ == '__main__':
    unittest.main()
