from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='pyOptional',
    use_scm_version=True,
    description='Library provided implementation Optional object similar to Java optional. Using this object, You will never check "if x is None"',
    long_description=long_description,
    url='https://github.com/PawelJ-PL/pyOptional',
    author='Pawel',
    author_email='inne.poczta@gmail.com',
    license='MIT',
    keywords='Python optional',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries'
    ],
    packages=find_packages(exclude=['tests']),
    extras_require={
        'test': ['coverage'],
    },
    setup_requires=['setuptools_scm'],
    python_requires='>=3',

)
