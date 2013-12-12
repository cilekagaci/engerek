# coding=utf-8
import jnius
from base import Deasciifier


TurkishDeasciifier = jnius.autoclass('turkish.Deasciifier')


class BalkansDeasciifier(Deasciifier):
    """A wrapper class that uses Balkan's Deasciifier"""

    def __init__(self):
        self.deasciifier = TurkishDeasciifier()

    def deasciify(self, text):
        """Returns deasciified version of a Turkish text.

        :param unicode text: ASCII text to be deasciified
        :returns unicode: Deasciified text
        """

        self.deasciifier.setAsciiString(text)
        return self.deasciifier.convertToTurkish().decode('utf-8')
