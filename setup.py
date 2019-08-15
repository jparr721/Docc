import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="docc",
    version="1.0.0",
    scripts=["bin/docc.py"],
    author="Jarred Parr",
    description="Docs that aren't trash",
    long_description=read("README.md")
)
