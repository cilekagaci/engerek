# coding=utf-8
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

version = '1.0-b'

install_requires = [
    'Cython>=0.19.2',
    'jnius>=1.1-dev',
    'regex>=2013-11-29',
]

setup(
    name='engerek',
    version=version,
    description='Turkish natural language processing tools for Python',
    long_description=README,
    classifiers=[
        'License :: Apache v2.0',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='turkish nlp tokenizer stemmer deasciifier',
    author=u'Çilek Ağacı',
    author_email='info@cilekagaci.com',
    url='http://cilekagaci.com/',
    license='Apache v2.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    dependency_links=['http://github.com/kivy/pyjnius/tarball/master#egg=jnius-1.1-dev'],
)
