import unittest
from postfixcalc import calc


class TestPostFixCalc(unittest.TestCase):

    def test_calc(self):
        self.assertEqual(calc('3 4 + 7 *'), 49)
        self.assertEqual(calc('5 5 + 10 * 20 /'), 5)
        self.assertEqual(calc('8 5 - 10 * 20 +'), 50)
        self.assertEqual(calc('5 10 - 5 *'), -25)

if __name__ == '__main__':
    unittest.main()
