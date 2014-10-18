import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

from docopt import __version__


class PyTestCommand(TestCommand):
    """ Command to run unit py.test unit tests
    """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest
        rcode = pytest.main(self.test_args)
        sys.exit(rcode)


setup(
    name='IPythonTOC',
    py_modules=['IPythonTOC'],
    version=__version__,
    author='Bren Letson',
    description='Class for generating markdown entries used for notebook TOC',
    url='http://bit.ly/1zge9gE',
    keywords='option arguments parsing optparse argparse getopt',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=[
            'pytest',
        ],
    cmdclass={
            'test': PyTestCommand,
        }
)
