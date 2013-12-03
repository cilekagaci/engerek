# coding=utf-8
import unittest
from engerek import ZemberekStemmer


class TestZemberekStemmer(unittest.TestCase):

    def test(self):
        stemmer = ZemberekStemmer()

        self.assertItemsEqual(stemmer.stem(u'atandı'),
                              ['atmak', 'atamak', 'ata'])


if __name__ == '__main__':
    unittest.main()
