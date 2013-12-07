# coding=utf-8
import unittest
from engerek import ZemberekStemmer


class TestZemberekStemmer(unittest.TestCase):

    def test_default(self):
        stemmer = ZemberekStemmer()

        self.assertListEqual(stemmer.stem(u'atandı'),
                             [u'at', u'ata', u'ata'])

        # Test stemming stopwords like 'bu', 'şu', etc.
        # Note that 'onlar' also means 'ondalık sayı sistemine göre yazılan bir
        # tam sayıda sağdan sola doğru ikinci basamağa verilen ad'.
        self.assertListEqual(stemmer.stem(u'bu'), [u'bu'])
        self.assertListEqual(stemmer.stem(u'bunlar'), [u'bu'])
        self.assertListEqual(stemmer.stem(u'şu'), [u'şu'])
        self.assertListEqual(stemmer.stem(u'şunlar'), [u'şu'])
        self.assertListEqual(stemmer.stem(u'o'), [u'o'])
        self.assertListEqual(stemmer.stem(u'onlar'), [u'o', u'onlar'])

    def test_prefer_infinitive_form(self):
        stemmer = ZemberekStemmer(prefer_infinitive_form=True)

        self.assertListEqual(stemmer.stem(u'atandı'),
                             [u'atmak', u'atamak', u'ata'])


if __name__ == '__main__':
    unittest.main()
