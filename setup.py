import re
from setuptools import setup
from codecs import open


#get version number from package init
with open('fake/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('fake/__init__.py', 'r') as fd:
    license = re.search(r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

#get readme
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

CLASSIFIERS = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy']


setup(name='FakePythonPackage',
      version=version,
      description='Empty python package',
      long_description=readme,
      url='https://github.com/erinxocon/FakePythonPackage',
      author="Erin O'Connell",
      author_email='erinocon5@gmail.com',
      license=license,
      packages=['fake'],
      zip_safe=False,
      classifiers=CLASSIFIERS)