# Filename: setup.py
from setuptools import setup, find_packages

import dabdemo

setup(
  name = "dabdemo",
  version = '0.1.0',
  author = 'Prakash',
  url = "https://github.com/prakashkancham/databricks.git",
  author_email = "prakash@123.com",
  description = "Utilities for Databricks",
  packages = find_packages(include = ["dabdemo"]),
  entry_points={"group_1": "run=dabdemo.__main__:main"},
  install_requires = ["setuptools"]
)