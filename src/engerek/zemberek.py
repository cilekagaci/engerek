# coding=utf-8
import jnius
from base import Stemmer


TurkiyeTurkcesi = jnius.autoclass('net.zemberek.tr.yapi.TurkiyeTurkcesi')
Zemberek = jnius.autoclass('net.zemberek.erisim.Zemberek')


class ZemberekStemmer(Stemmer):
    LANGUAGE = TurkiyeTurkcesi()
    ZEMBEREK = Zemberek(LANGUAGE)
    ROOT_FINDER = ZEMBEREK.kokBulucu()

    IGNORED_TYPES = {
        'BAGLAC',
        'EDAT',
        'IMEK',
        'SORU',
        'ZAMIR',
    }

    @staticmethod
    def infinitive(word):
        suffix = ''
        for letter in reversed(word):
            if letter in {u'a', u'ı', u'o', u'u'}:
                suffix = 'mak'
                break
            if letter in {u'e', u'i', u'ö', u'ü'}:
                suffix = 'mek'
                break
        return word + suffix

    def stem(self, word):
        roots = self.ROOT_FINDER.kokBul(word)
        if len(roots) == 0:
            yield word
        for root in roots:
            type = root.tip().toString()
            if type in self.IGNORED_TYPES:
                continue
            if type == 'FIIL':
                yield self.infinitive(root.icerik())
            else:
                yield root.icerik()
