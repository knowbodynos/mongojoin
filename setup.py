#!/shared/apps/python/Python-2.7.5/INSTALL/bin/python

from setuptools import setup;

setup(name='mongolink',
      version='1.0',
      description='A package that allows a continuous non-blocking read of large batches of documents from a MongoDB database (remote or local), with some action performed on each batch.',
      url='https://github.com/knowbodynos/mongolink',
      author='Ross Altman',
      author_email='knowbodynos@gmail.com',
      license='GPLv3',
      packages=['mongolink'],
      zip_safe=False);