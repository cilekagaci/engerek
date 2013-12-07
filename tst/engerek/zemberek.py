# coding=utf-8
import unittest
from engerek import ZemberekStemmer


class TestZemberekStemmer(unittest.TestCase):

    def test_default(self):
        stemmer = ZemberekStemmer()

        self.assertItemsEqual(stemmer.stem(u'atandı'),
                              ['at', 'ata', 'ata'])

    def test_prefer_infinitive_form(self):
        stemmer = ZemberekStemmer(prefer_infinitive_form=True)

        self.assertItemsEqual(stemmer.stem(u'atandı'),
                              ['atmak', 'atamak', 'ata'])


if __name__ == '__main__':
    unittest.main()
