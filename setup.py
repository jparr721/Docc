import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="docc",
    version="2.0.1",
    scripts=["bin/docc"],
    author="Jarred Parr",
    description="Docs that aren't trash",
    long_description=read("README.md")
)
