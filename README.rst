Engerek: Turkish NLP Library for Python
=======================================

Engerek is an Apache v2.0 licensed Python library that brings together
commonly used natural language processing techniques, with a special
focus on Turkish text. Our aim is to provide a clean and consistent
interface for existing open source Turkish processing libraries.

Features
--------

-  Tokenize text (Engerek's own tokenizer that recognizes hashtags, user
   mentions, URLs and e-mail addresses)
-  Stem words (`via Zemberek <<https://code.google.com/p/zemberek/>`_)
-  Deasciify Turkish text that is written only by ASCII characters (`via
   Ahmet Alp Balkan's
   deasciifier <https://code.google.com/p/turkish-deasciifier/>`_)

Installation
------------

Engerek depends on the version 1.1-dev of Java access library PyJNius,
which currently cannot be installed using ``pip``. You should install
PyJNius manually from the repository. Other dependencies will be
installed automatically by the setup script.

::

    $ pip install git+git://github.com/cilekagaci/engerek.git#egg=engerek
    $ git clone https://github.com/kivy/pyjnius/
    $ cd pyjnius
    $ python setup.py install

Engerek also depends on third-party Java libraries. You should download
these yourself and place them somewhere in your class path.

::

    $ mkdir -p $HOME/lib
    $ cd $HOME/lib
    $ wget https://zemberek.googlecode.com/files/zemberek-2.1.1.zip
    $ unzip zemberek-2.1.1.zip
    $ mv jar/*.jar .
    $ rm -r belgeler
    $ rm -r jar
    $ rm surumler.txt
    $ rm zemberek-2.1.1.zip
    $ wget https://turkish-deasciifier.googlecode.com/files/turkish-deasciifier-1.0.jar
    $ export CLASSPATH=$CLASSPATH:$HOME/lib/*

Now, you can check if the installation works.

::

    >>> from engerek import *

Usage
-----

::

    >>> from engerek import *
    >>> deasciifier = BalkansDeasciifier()
    >>> print deasciifier.deasciify(u'Hadi bir masal uyduralim, icinde mutlu, doygun, telassiz durdugumuz.')
    Hadi bir masal uyduralım, içinde mutlu, doygun, telaşsız durduğumuz.
    >>> tokenizer.tokenize(u'Hadi bir masal uyduralım, içinde mutlu, doygun, telaşsız durduğumuz.')
    [u'Hadi', u'bir', u'masal', u'uydural\u0131m', u'i\xe7inde', u'mutlu', u'doygun', u'tela\u015fs\u0131z', u'durdu\u011fumuz']
    >>> stemmer = ZemberekStemmer(prefer_infinitive_form=True)
    >>> print stemmer.stem(u'atandı')
    [u'atmak', u'atamak', u'ata']

