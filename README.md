# Advent of Code

![](https://github.com/jswarburton/advent-of-code-2023/workflows/Python%20CI/badge.svg)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)

Python solutions for [Advent of Code](https://adventofcode.com) 🎄🎅

For descriptions of the puzzles see the website.

## Setting up local dev environment

    pyenv virtualenv 3.13 aoc
    pyenv activate aoc
    pip install -r test-requirements.txt

## Running tests and checking formatting

Tests and formatting checks can be run locally in the activated `pyenv` environment:

    tox

To reformat run:

    tox -e format
