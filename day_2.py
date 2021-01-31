#!/usr/bin/env python3
"""
Template for Python solution
"""

from aocd import submit
import fileinput
import sys

class Intcode():
    def __init__(self, init):
        self.intcode = [int(x) for x in init]
        self.idx = 0

    def __len__(self):
        return len(self.intcode)

    def __getitem__(self, key):
        return self.intcode[key]

    def __setitem__(self, key, value):
        self.intcode[key] = value

    def __repr__(self):
        return f'Intcode:\nIdx = {self.idx}\n{self.intcode}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.intcode):
            raise StopIteration
        current = self.intcode[self.idx]
        self.idx += 1
        return current

    def jump(self, steps):
        assert steps >= 0, "Step must be non-negative"
        self.idx += steps

    def process(self, args):
        assert len(args) == 4
        opcode, addr = args[0], args[1:]
        if opcode == 1:
            self.intcode[addr[-1]] = self.intcode[addr[0]] + self.intcode[addr[1]]
        elif opcode == 2:
            self.intcode[addr[-1]] = self.intcode[addr[0]] * self.intcode[addr[1]]
        elif opcode == 99:
            raise StopIteration
        else:
            raise RuntimeError

if __name__ == '__main__':
    intcode = Intcode(fileinput.input().readline().split(','))
    #intcode = [int(x) for x in fileinput.input().readline().split(',')]

    # Part 1
    intcode[1] = 12
    intcode[2] = 2

    ## Solution with my Intcode class
    while intcode.idx < len(intcode):
        args = intcode[intcode.idx:intcode.idx + 4]
        try:
            intcode.process(args)
            intcode.jump(4)
        except StopIteration:
            break
        except RuntimeError:
            print(f'An error occurred!')
            break

    ## Solution with bare python
    #idx = 0
    #while idx < len(intcode):
    #    code = intcode[idx]
    #    if code == 99:
    #        break
    #    elif code == 1:
    #        intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] + intcode[intcode[idx + 2]]
    #    elif code == 2:
    #        intcode[intcode[idx + 3]] = intcode[intcode[idx + 1]] * intcode[intcode[idx + 2]]
    #    idx += 4

    print(intcode)

