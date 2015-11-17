import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        pass

    def test_five(self):
        self.assertEqual(fizzbuzz(10), 'Buzz')

    def test_three_five(self):
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')

    def test_three(self):
        self.assertEqual(fizzbuzz(6), 'Fizz')

    def test_none(self):
        self.assertEqual(fizzbuzz(8), str(8))

if __name__ == '__main__':
    unittest.main()
