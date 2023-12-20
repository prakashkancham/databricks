# Filename: setup.py
from setuptools import setup, find_packages

import dabdemo

setup(
  name = "dabdemo",
  version = 'dabdemo.0.1',
  author = 'dabdemo.prakash',
  url = "https://github.com/prakashkancham/databricks.git",
  author_email = "<my-author-name>@<my-organization>",
  description = "<my-package-description>",
  packages = find_packages(include = ["dabdemo"]),
  entry_points={"group_1": "run=dabdemo.__main__:main"},
  install_requires = ["setuptools"]
)