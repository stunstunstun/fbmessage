#!/usr/bin/env python
import fbmessage
import os.path
from setuptools import find_packages, setup


def readme():
    path = os.path.join(os.path.dirname(__file__), 'README.md')
    try:
        with open(path) as f:
            return f.read()
    except IOError:
        pass


def install():
    setup(
        name='fbmessage',
        version=fbmessage.__version__,
        description=fbmessage.__doc__,
        long_description=readme(),
        url='https://github.com/wjdsupj/fbmessage',
        author='agileboys.com',
        author_email='agileboys@gmail.com',
        license='MIT',
        classifiers=['Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Education',
                     'Intended Audience :: End Users/Desktop',
                     'License :: Freeware',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Education',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6'],
        packages=find_packages(exclude=['docs', 'tests']),
        keywords='facebook messenger message',
        install_requires=[
            'requests',
        ],
        extras_require={
            'h2': ['hyper'],
        },
        tests_require=[
            'pytest',
            'coveralls',
        ]
    )


if __name__ == "__main__":
    install()
