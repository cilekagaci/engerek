# coding=utf-8
import jnius
from base import Stemmer
from common import infinitive_form


TurkiyeTurkcesi = jnius.autoclass('net.zemberek.tr.yapi.TurkiyeTurkcesi')
Zemberek = jnius.autoclass('net.zemberek.erisim.Zemberek')


class ZemberekStemmer(Stemmer):
    """Wrapper class for Zemberek's kokBulucu (Root finder)"""

    LANGUAGE = TurkiyeTurkcesi()
    ZEMBEREK = Zemberek(LANGUAGE)
    ROOT_FINDER = ZEMBEREK.kokBulucu()

    def __init__(self, prefer_infinitive_form=False):
        #: If prefer_infinitive_form is set to true verb stems will be
        #: returned in infinitive form
        self.prefer_infinitive_form = prefer_infinitive_form

    def stem(self, word):
        """Finds the stem of a word.

        :param unicode word: The word to be stemmed
        :returns list: A list of unicode strings which contain possible
        stems of the word
        """

        roots = self.ROOT_FINDER.kokBul(word)

        if len(roots) == 0:
            return [word]

        stems = []
        for root in roots:
            stem = root.icerik().decode('utf-8')
            type = root.tip().toString()
            if self.prefer_infinitive_form and type == 'FIIL':
                stems.append(infinitive_form(stem))
            else:
                stems.append(stem)

        return stems
