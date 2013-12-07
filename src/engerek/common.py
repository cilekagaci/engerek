# coding=utf-8


FRONT_VOWELS = {u'e', u'i', u'ö', u'ü'}
BACK_VOWELS = {u'a', u'ı', u'o', u'u'}


def infinitive_form(verb):
    for letter in reversed(verb):
        if letter in FRONT_VOWELS:
            return verb + 'mek'
        if letter in BACK_VOWELS:
            return verb + 'mak'
    return verb
