# coding=utf-8
import unittest
from engerek import ZemberekStemmer


class TestZemberekStemmer(unittest.TestCase):

    def test_default(self):
        stemmer = ZemberekStemmer()

        self.assertItemsEqual(stemmer.stem(u'atandı'),
                              ['at', 'ata', 'ata'])

        # Test stemming stopwords like 'bu', 'şu', etc.
        # Note that 'onlar' also means 'ondalık sayı sistemine göre yazılan bir
        # tam sayıda sağdan sola doğru ikinci basamağa verilen ad'.
        self.assertItemsEqual(stemmer.stem(u'bu'), ['bu'])
        self.assertItemsEqual(stemmer.stem(u'bunlar'), ['bu'])
        self.assertItemsEqual(stemmer.stem(u'şu'), ['şu'])
        self.assertItemsEqual(stemmer.stem(u'şunlar'), ['şu'])
        self.assertItemsEqual(stemmer.stem(u'o'), ['o'])
        self.assertItemsEqual(stemmer.stem(u'onlar'), ['o', 'onlar'])

    def test_prefer_infinitive_form(self):
        stemmer = ZemberekStemmer(prefer_infinitive_form=True)

        self.assertItemsEqual(stemmer.stem(u'atandı'),
                              ['atmak', 'atamak', 'ata'])


if __name__ == '__main__':
    unittest.main()
