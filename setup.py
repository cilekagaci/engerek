# coding=utf-8


# Copyright 2013-2014 Eser Aygün & Amaç Herdağdelen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

version = '1.0-b'

install_requires = [
    'Cython>=0.19.2',
    #'jnius>=1.1-dev',  # currently not available via PyPI
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
)
