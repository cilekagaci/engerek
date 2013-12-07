# coding=utf-8
import unittest
from engerek import EngerekTokenizer


class TestEngerekTokenizer(unittest.TestCase):

    def test_default(self):
        tokenizer = EngerekTokenizer()

        self.assertListEqual(
            tokenizer.tokenize(
                u'Hadi bir masal uyduralım, içinde mutlu, doygun, telaşsız'
                u' durduğumuz.'
            ),
            [
                u'Hadi', u'bir', u'masal', u'uyduralım', u'içinde', u'mutlu',
                u'doygun', u'telaşsız', u'durduğumuz',
            ],
        )
        self.assertListEqual(
            tokenizer.tokenize(
                u"Kılıç'tan 'Yüce Atatürk' açıklaması: T.F.F.'nin kararı"
                u" toplumu böler"
            ),
            [
                u"Kılıç'tan", u'Yüce', u'Atatürk', u'açıklaması',
                u"T.F.F.'nin", u'kararı', u'toplumu', u'böler',
            ],
        )
        self.assertListEqual(
            tokenizer.tokenize(
                u'#Türkiye @buse http://tr.vineo.me/vine/12345 …'
            ),
            [
                u'#Türkiye', u'@buse', u'http://tr.vineo.me/vine/12345',
            ],
        )
        self.assertListEqual(
            tokenizer.tokenize(
                u'+nasılsın anneanne :) - iyi be yavrum ıhıhıhıh sen nabiyosun'
                u' ıhıhıhıh :d:d'
            ),
            [
                u'nasılsın', u'anneanne', u':)', u'iyi', u'be', u'yavrum',
                u'ıhıhıhıh', u'sen', u'nabiyosun', u'ıhıhıhıh', u':d', u':d'
            ],
        )

    def test_strip_apostrophe_suffixes(self):
        tokenizer = EngerekTokenizer(strip_apostrophe_suffixes=True)

        self.assertListEqual(
            tokenizer.tokenize(
                u"Kılıç'tan 'Yüce Atatürk' açıklaması: T.F.F.'nin kararı"
                u" toplumu böler"
            ),
            [
                u'Kılıç', u'Yüce', u'Atatürk', u'açıklaması',
                u'T.F.F.', u'kararı', u'toplumu', u'böler',
            ],
        )


if __name__ == '__main__':
    unittest.main()
