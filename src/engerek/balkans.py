# coding=utf-8
import jnius
from base import Deasciifier


TurkishDeasciifier = jnius.autoclass('turkish.Deasciifier')


class BalkansDeasciifier(Deasciifier):
    """A Turkish deasciifier based on Balkan's deasciifier library."""

    def __init__(self):
        """Creates a BalkansDeasciifier."""
        self.deasciifier = TurkishDeasciifier()

    def deasciify(self, text):
        """Returns the deasciified version of the given text.

        :param text: ASCII text to be deasciified
        :type text: str or unicode
        :return: deasciified text
        :rtype: unicode
        """

        self.deasciifier.setAsciiString(text)
        return self.deasciifier.convertToTurkish().decode('utf-8')
