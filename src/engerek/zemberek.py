# coding=utf-8
import jnius
from base import Stemmer
from common import infinitive_form


TurkiyeTurkcesi = jnius.autoclass('net.zemberek.tr.yapi.TurkiyeTurkcesi')
Zemberek = jnius.autoclass('net.zemberek.erisim.Zemberek')


class ZemberekStemmer(Stemmer):
    """Turkish stemmer based on Zemberek library."""

    LANGUAGE = TurkiyeTurkcesi()
    ZEMBEREK = Zemberek(LANGUAGE)
    ROOT_FINDER = ZEMBEREK.kokBulucu()

    def __init__(self, prefer_infinitive_form=False):
        """Creates a ZemberekStemmer.

        :param prefer_infinitive_form: return verb stems in infinitive form if
            ``True``; otherwise return only the root (default value is
            ``False``)
        :type prefer_infinitive_form: bool
        """
        self.prefer_infinitive_form = prefer_infinitive_form

    def stem(self, word):
        """Finds the stem of the given word.

        :param word: word to be stemmed
        :type word: unicode
        :return: list of possible stems of the word
        :rtype: list of unicode
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
