# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="trigrams",
    description="Trigrams",
    version='0.1.0',
    author="Jeff Torres",
    author_email="jeffrey.n.torres@gmail.com",
    license='MIT',
    py_modules=['trigrams'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ["pytest", "pytest-watch", "pytest-cov", "tox"]},
)
