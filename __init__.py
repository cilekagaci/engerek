# coding=utf-8
import atexit
import jpype


class_path = [
    'lib/zemberek-cekirdek-2.1.1.jar',
    'lib/zemberek-tr-2.1.1.jar'
]
jpype.startJVM('/usr/lib/jvm/java-7-oracle/jre/lib/amd64/server/libjvm.so',
               '-Djava.class.path=%s' % ':'.join(class_path))

zemberek = jpype.JPackage('net').zemberek


def finalize():
    jpype.shutdownJVM()


atexit.register(finalize)


class ZemberekStemmer(object):
    LANGUAGE = zemberek.tr.yapi.TurkiyeTurkcesi()
    ZEMBEREK = zemberek.erisim.Zemberek(LANGUAGE)
    ROOT_FINDER = ZEMBEREK.kokBulucu()

    IGNORED_TYPES = {
        zemberek.yapi.KelimeTipi.BAGLAC,
        zemberek.yapi.KelimeTipi.EDAT,
        zemberek.yapi.KelimeTipi.IMEK,
        zemberek.yapi.KelimeTipi.SORU,
        zemberek.yapi.KelimeTipi.ZAMIR,
    }

    @staticmethod
    def infinitive(word):
        suffix = ''
        for letter in reversed(word):
            if letter in {u'a', u'ı', u'o', u'u'}:
                suffix = 'mak'
                break
            if letter in {u'e', u'i', u'ö', u'ü'}:
                suffix = 'mek'
                break
        return word + suffix

    def stem(self, word):
        roots = self.ROOT_FINDER.kokBul(word)
        if len(roots) == 0:
            yield word
        for root in roots:
            type = root.tip()
            if type in self.IGNORED_TYPES:
                continue
            if type == zemberek.yapi.KelimeTipi.FIIL:
                yield self.infinitive(root.icerik())
            else:
                yield root.icerik()
