# coding=utf-8
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '1.0-a'

install_requires = [
    'jnius==1.1-dev',
    'Cython==0.19.2',
    'regex',
]

setup(
    name='engerek',
    version=version,
    description='Turkish natural language processing tools for Python',
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'License :: Apache v2.0',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='turkish nlp tokenizer stemmer deasciifier',
    author=u'Çilek Ağacı',
    author_email='info@cilekagaci.com',
    url='http://cilekagaci.com/',
    license='Proprietary',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    dependency_links=['http://github.com/kivy/pyjnius/tarball/master#egg=jnius-1.1-dev'],
)
