# coding=utf-8
import jnius
from base import Stemmer
from common import infinitive_form


TurkiyeTurkcesi = jnius.autoclass('net.zemberek.tr.yapi.TurkiyeTurkcesi')
Zemberek = jnius.autoclass('net.zemberek.erisim.Zemberek')


class ZemberekStemmer(Stemmer):
    LANGUAGE = TurkiyeTurkcesi()
    ZEMBEREK = Zemberek(LANGUAGE)
    ROOT_FINDER = ZEMBEREK.kokBulucu()

    def __init__(self, prefer_infinitive_form=False):
        self.prefer_infinitive_form = prefer_infinitive_form

    def stem(self, word):
        roots = self.ROOT_FINDER.kokBul(word)
        if len(roots) == 0:
            yield word
        for root in roots:
            type = root.tip().toString()
            if self.prefer_infinitive_form and type == 'FIIL':
                yield infinitive_form(root.icerik())
            else:
                yield root.icerik()
