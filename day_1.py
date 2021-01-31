#!/usr/bin/env python3
"""
Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""

import fileinput
from aocd import submit

def get_fuel(n):
    tot = []
    x = n
    while x > 0:
        x = (x // 3) - 2
        tot.append(x)
    return sum([y for y in tot if y > 0])

if __name__ == '__main__':
    lines = [*fileinput.input()]
    ans = 0
    for n in lines:
        ans += (int(n) // 3) - 2
    print(f'Part 1: {ans}')

    ans2 = 0
    for n in lines:
        ans2 += get_fuel(int(n))
    print(f'Part 2: {ans2}')
