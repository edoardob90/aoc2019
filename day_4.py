#!/usr/bin/env python3
"""
Day 4: Secure Container
https://adventofcode.com/2019/day/4
"""

import fileinput
from aoc import timer
import re

def tally(l):
# A function to group each element of a list by its multiplicity (how many time it appears)
    d = {}
    for i in l:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d

@timer
def solve(p2=False):
    my_range = range(136760, 595730 + 1)
    count = 0
    for pwd in my_range:
        pwd_str = str(pwd)
        if list(pwd_str) == sorted(list(pwd_str)):
            if not p2 and not ( len(pwd_str) == len(set(pwd_str)) ):
                count += 1
            # Explanation:
            #  tally(num) returns a dict with each digit and how many times it appears
            #  I get the values and convert to a list
            #  Then I count how many "2" there are: there must be either 1 or more
            #  If there's an ODD number of "2", then it means that either no repeated digits are present (invalid) or that a pair of digits is part of a larger group (e.g. 444)
            elif list(tally(list(pwd_str)).values()).count(2) >= 1:
                count += 1
    return count

if __name__ == '__main__':
    print("======= Part 1 =======")
    count = solve()
    print(f'Number of valid passwords: {count}\n')

    print("======= Part 2 =======")
    count = solve(True)
    print(f'Number of valid passwords: {count}')
