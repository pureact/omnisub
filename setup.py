"""Setup for omnisub."""

from distutils.core import setup
from setuptools import find_packages

setup(
    name="omnisub",
    version="1.0",
    description="omnisub",
    author="naek",
    packages=find_packages(),
    entry_points={"console_scripts": ["omnisub=omnisub.__main__:main"]},
)
