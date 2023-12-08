# Advent of Code 2023

![](https://github.com/jswarburton/advent-of-code-2023/workflows/Python%20CI/badge.svg)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

Python solutions for [Advent of Code 2023](https://adventofcode.com/2023) 🎄🎅

For descriptions of the puzzles see the website.

## Setting up local dev environment

    conda create -n aoc python=3.9
    conda activate aoc
    pip install -r test-requirements.txt

## Running tests and checking formatting

Tests and formatting checks can be run locally in the activated `conda` environment:

    tox

To reformat run:

    tox -e format
