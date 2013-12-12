Engerek
========
Turkish natural language processing library
--------------------------------------------

Engerek is a Python library that brings together commonly used natural language processing techniques, with a special focus on Turkish text.

Our aim is to provide a clean and consistent interface for existing open source Turkish processing libraries.

Currently you can

- tokenize text (Engerek's own tokenizer that recognizes hashtags, user mentions, URLs)
- stem words ([via Zemberek](<https://code.google.com/p/zemberek/))
- deasciify Turkish text that is written only by ASCII characters ([via Ahmet Balkan's deasciifier](https://code.google.com/p/turkish-deasciifier/))

Usage
-----

```python
>>> from engerek import *
>>> deasciifier = BalkansDeasciifier()
>>> print deasciifier.deasciify(u'Hadi bir masal uyduralim, icinde mutlu, doygun, telassiz durdugumuz.')
Hadi bir masal uyduralım, içinde mutlu, doygun, telaşsız durduğumuz.
>>> tokenizer.tokenize(u"Hadi bir masal uyduralım, içinde mutlu, doygun, telaşsız durduğumuz.")
[u'Hadi', u'bir', u'masal', u'uydural\u0131m', u'i\xe7inde', u'mutlu', u'doygun', u'tela\u015fs\u0131z', u'durdu\u011fumuz']
>>> stemmer = ZemberekStemmer(prefer_infinitive_form=True)
>>> print stemmer.stem(u'atandı')
[u'atmak', u'atamak', u'ata']
```

Installation and Setup
----------------------
Install Python dependencies and Engerek.
```sh
$ pip install cython
$ pip install git+git://github.com/cilekagaci/engerek.git#egg=engerek
```

In the last above step, if you get a failure about missing Cython.Distutils just re-run the same command.

Download Balkan's deasciifier and Zemberek libraries as jar files and put them under a directory in your Java classpath.
```sh
$ mkdir -p $HOME/lib && cd $HOME/lib
$ wget https://zemberek.googlecode.com/files/zemberek-2.1.1.zip
$ unzip zemberek-2.1.1.zip && rm zemberek-2.1.1.zip
$ mv jar/*.jar .
$ rm -r belgeler
$ rm -r jar
$ rm surumler.txt
$ wget https://turkish-deasciifier.googlecode.com/files/turkish-deasciifier-1.0.jar
$ export CLASSPATH=$CLASSPATH:$HOME/lib/*
```

Check if the installation works:
```python
>>> from engerek import *
```
