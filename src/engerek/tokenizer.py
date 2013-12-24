# coding=utf-8
import regex
from base import Tokenizer


class AdvancedScanner(regex.Scanner):

    def scan(self, string):
        result = []
        append = result.append
        match = self.scanner.scanner(string).match
        i = 0
        while True:
            m = match()
            if not m:
                break
            j = m.end()
            if i == j:
                break
            action = self.lexicon[m.lastindex - 1][1]
            if hasattr(action, '__call__'):
                self.match = m
                action = action(self, string, m)
            if action is not None:
                append(action)
            i = j

        return result, string[i:]


class Token(object):
    ignore = False

    def __init__(self, scanner, string, left, right):
        self.scanner = scanner
        self.type = type(self).__name__
        self.string = string
        self.left = left
        self.right = right

    @classmethod
    def get_pattern(cls):
        return ur'.'

    @classmethod
    def get_action(cls):
        if cls.ignore:
            return lambda scanner, string, match: None
        else:
            return lambda scanner, string, match:\
                cls(scanner, match.group(),
                    match.start(), len(string) - match.end())

    @classmethod
    def lexeme(cls):
        return cls.get_pattern(), cls.get_action()


class BaseEngerekTokenizer(Tokenizer):
    lexicon = []

    def __init__(self):
        self.scanner = AdvancedScanner(
            [t.lexeme() for t in self.lexicon],
            regex.UNICODE | regex.IGNORECASE
        )

    def _tokenize(self, text):
        tokens, rest = self.scanner.scan(text)
        for token in tokens:
            yield token

    def tokenize(self, text):
        return [t.string for t in self._tokenize(text)]


class PatternToken(Token):
    pattern = ur'.'

    @classmethod
    def get_pattern(cls):
        return cls.pattern

    @classmethod
    def lexeme(cls):
        return cls.get_pattern(), cls.get_action()


class EmoticonToken(Token):
    alternatives = []

    @classmethod
    def get_pattern(cls):
        patterns = []
        for alternative in cls.alternatives:
            pattern = regex.escape(alternative)
            if regex.fullmatch(ur'\w', alternative[-1]):
                pattern += ur'\b'
            patterns.append(pattern)
        return '|'.join(patterns)


class UrlToken(PatternToken):
    pattern = ur'[A-Z0-9]+([+\-][A-Z0-9]+)*://\S+'


class EmailAddressToken(PatternToken):
    pattern = ur'[A-Z0-9_]+([+\-.][A-Z0-9_]+)*' \
              ur'@[A-Z0-9]+([+\-.][A-Z0-9]+)*\.[A-Z0-9]+'


class UserNameToken(PatternToken):
    pattern = ur'@\w+'


class HashTagToken(PatternToken):
    pattern = ur'#\w+'


class NumberToken(PatternToken):
    pattern = ur'\d+([.,:\-]\d+)*'


class WordToken(PatternToken):
    pattern = ur'([^\W\d]\.){2,}|[^\W\d]+|&'


class ApostropheToken(PatternToken):
    pattern = ur"['’]"


class SuffixToken(WordToken):
    pattern = ur"['’]([^\W\d]+|&)"


class WhitespaceToken(PatternToken):
    pattern = ur'\s+'


class OtherToken(PatternToken):
    pattern = ur'.'


class HappyToken(EmoticonToken):
    alternatives = [
        ':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
        ':^)', ":')",
    ]


class LaughingToken(EmoticonToken):
    alternatives = [
        ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D', '=-3',
        '=3', 'B^D',
    ]


class SadToken(EmoticonToken):
    alternatives = [
        ':-(', ':(', '>:[', ':-c', ':c', ':-<', ':<', ':-[', ':[', ':{',
    ]


class AngryToken(EmoticonToken):
    alternatives = [
        ':-||', ':@',
    ]


class CryingToken(EmoticonToken):
    alternatives = [
        ":'-(", ":'(",
    ]


class SurprisedToken(EmoticonToken):
    alternatives = [
        '>:O', ':-O', ':O', ':O', 'o_O', 'o_0', 'o.O', '8-0',
    ]


class KissingToken(EmoticonToken):
    alternatives = [
        ':*', ':^*', ':^',
    ]


class WinkingToken(EmoticonToken):
    alternatives = [
        ';-)', ';)', '*-)', '*)', ';-]', ';]', ';D', ';^)',
    ]


class CheekyToken(EmoticonToken):
    alternatives = [
        '>:P', ':-P', ':P', 'X-P', 'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b',
        ':b',
    ]


class AnnoyedToken(EmoticonToken):
    alternatives = [
        '>:\\', '>:/', ':-/', ':-.', ':/', ':\\', '=/', '=\\', ':L', '=L',
        ':S',
    ]


class StraightToken(EmoticonToken):
    alternatives = [
        ':-|', ':|',
    ]


class EmbarrassedToken(EmoticonToken):
    alternatives = [
        ':$',
    ]


class LoveToken(EmoticonToken):
    alternatives = [
        '<3',
    ]


class EngerekTokenizer(BaseEngerekTokenizer):
    lexicon = [
        HappyToken,
        LaughingToken,
        SadToken,
        AngryToken,
        CryingToken,
        SurprisedToken,
        KissingToken,
        WinkingToken,
        CheekyToken,
        AnnoyedToken,
        StraightToken,
        EmbarrassedToken,
        LoveToken,

        UrlToken,
        EmailAddressToken,
        UserNameToken,
        HashTagToken,
        NumberToken,
        WordToken,
        ApostropheToken,
        WhitespaceToken,
        OtherToken,
    ]

    @staticmethod
    def _concat_tokens(cls, *tokens):
        scanner = tokens[0].scanner
        string = ''.join(t.string for t in tokens)
        left = tokens[0].left
        right = tokens[-1].right
        return cls(scanner, string, left, right)

    def __init__(self, strip_apostrophe_suffixes=False):
        super(EngerekTokenizer, self).__init__()
        self.strip_apostrophe_suffixes = strip_apostrophe_suffixes

    def _tokenize(self, text):
        tokens, rest = self.scanner.scan(text)
        history = [None, None]
        for token in tokens:
            # Ignore whitespace and apostrophes.
            if type(token) not in [WhitespaceToken, OtherToken,
                                   ApostropheToken]:

                # Yield any whitespace preceding the current token.
                whitespace = []
                for previous_token in reversed(history):
                    if type(previous_token) in [WhitespaceToken, OtherToken]:
                        whitespace.append(previous_token)
                    else:
                        break
                if whitespace:
                    yield self._concat_tokens(WhitespaceToken, *whitespace)

                # Handle apostrophe suffixes.
                # An apostrophe suffix is a word following an apostrophe
                # following another word.
                if type(token) == WordToken \
                        and type(history[-1]) == ApostropheToken \
                        and type(history[-2]) == WordToken:
                    yield self._concat_tokens(SuffixToken, history[-1], token)
                else:
                    yield token

            history.append(token)

    def _filtered(self, text):
        tokens = list(self._tokenize(text))
        for index, token in enumerate(tokens):
            # Glue apostrophe suffixes to the preceding token if requested.
            if not self.strip_apostrophe_suffixes \
                    and index < len(tokens) - 1 \
                    and type(tokens[index + 1]) == SuffixToken:
                yield self._concat_tokens(WordToken, token, tokens[index + 1])
            # Skip whitespace and apostrophe suffixes.
            elif type(token) not in [WhitespaceToken, OtherToken,
                                     ApostropheToken, SuffixToken]:
                yield token

    def tokenize(self, text):
        return [t.string for t in self._filtered(text)]
