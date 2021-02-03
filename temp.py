#!/usr/bin/env python3
"""
Template for Python solution
"""

import fileinput
from aoc import timer

def process():
    pass

if __name__ == '__main__':
    lines = [*fileinput.input()]
    process(lines)
    submit(my_answer, part="a", day=1, year=2019)
