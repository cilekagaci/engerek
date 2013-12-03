from abc import abstractmethod


class Stemmer(object):

    @abstractmethod
    def stem(self, word):
        raise NotImplementedError()
