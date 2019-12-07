#!/usr/bin/env python
import os
from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

packages = None
package_data = None
zip_safe = True

class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

cmdclass = {'test': PyTest}

setup(
    name='SoundFile',
    version='0.10.3post1',
    description='An audio library based on libsndfile, CFFI and NumPy',
    author='Bastian Bechtold',
    author_email='basti@bastibe.de',
    url='https://github.com/bastibe/PySoundFile',
    keywords=['audio', 'libsndfile'],
    py_modules=['soundfile'],
    packages=packages,
    package_data=package_data,
    zip_safe=zip_safe,
    license='BSD 3-Clause License',
    setup_requires=["cffi>=1.0"],
    install_requires=['cffi>=1.0'],
    cffi_modules=["soundfile_build.py:ffibuilder"],
    extras_require={'numpy': ['numpy']},
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Multimedia :: Sound/Audio',
    ],
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    tests_require=['pytest'],
    cmdclass=cmdclass,
)
