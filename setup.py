"""Setup for omnisub."""

from distutils.core import setup

setup(
    name="omnisub",
    version="1.0",
    description="omnisub",
    author="naek",
    packages=["omnisub", "omnisub.omnisub"],
    entry_points={"console_scripts": ["omnisub=omnisub.__main__:main"]},
)
