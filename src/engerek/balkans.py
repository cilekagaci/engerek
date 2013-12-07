# coding=utf-8
import jnius
from base import Deasciifier


TurkishDeasciifier = jnius.autoclass('turkish.Deasciifier')


class BalkansDeasciifier(Deasciifier):

    def __init__(self):
        self.deasciifier = TurkishDeasciifier()

    def deasciify(self, text):
        self.deasciifier.setAsciiString(text)
        return self.deasciifier.convertToTurkish().decode('utf-8')
