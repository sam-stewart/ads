import unittest
from wordladder import wordladder
import string

class TestWordLadder(unittest.TestCase):

    def setUp(self):
        f = open('dictionary.txt', 'r')
        self.lexicon = { line.strip().lower().translate(None, string.punctuation)
                        for line in f }
        f.close()
        self.base = 'grass'
        self.target = 'tipsy'
        self.expected = ['grass', 'crass', 'cross', 'crops', 'coops',
                         'loops', 'loopy', 'loppy', 'lippy', 'tippy',
                         'tipsy']
        self.maxDiff = None

    def test_wordladder(self):
        ladder = wordladder(self.base, self.target, self.lexicon)
        self.assertEqual(ladder, self.expected)

    def test_wordladder_fail(self):
        ladder = wordladder('ninja', 'baldy', self.lexicon)
        self.assertIsNone(ladder)

if __name__ == '__main__':
    unittest.main()
