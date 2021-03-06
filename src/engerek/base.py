from abc import abstractmethod


class Deasciifier(object):

    @abstractmethod
    def deasciify(self, text):
        raise NotImplementedError()


class Tokenizer(object):

    @abstractmethod
    def tokenize(self, text):
        raise NotImplementedError()


class Stemmer(object):

    @abstractmethod
    def stem(self, word):
        raise NotImplementedError()
