#!/usr/bin/env python3
"""
Day 5: Sunny with a Chance of Asteroids
https://adventofcode.com/2019/day/5
"""

import fileinput
import sys
from aoc import read_file

class Intcode():
    def __init__(self, init, input_value):
        if not isinstance(init, list):
            raise TypeError
        self.intcode = [int(x) for x in init]
        self.idx = 0 # instruction pointer
        self.input = input_value

    def reset(self, init, noun=12, verb=2):
        self.idx = 0
        self.intcode = [int(x) for x in init]
        self.intcode[1] = noun
        self.intcode[2] = verb

    def __len__(self):
        return len(self.intcode)

    def __getitem__(self, key):
        return self.intcode[key]

    def __setitem__(self, key, value):
        self.intcode[key] = value

    def __repr__(self):
        intcode_str = ''
        for i,v in enumerate(self.intcode):
            intcode_str += f'Intcode({i}) = {v}\n'
        return f'Intcode:\nLast idx = {self.idx}\n{intcode_str}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.intcode):
            raise StopIteration
        current = self.intcode[self.idx]
        self.idx += 1
        return current

    def parse_modes(self, modes, args):
        # parameter modes: how do we interpret the args?
        # 0 => arg is ADDRESS (position mode)
        # 1 => arg is VALUE (immediate mode)
        m = modes[1:]
        if m == '00':
            return self.intcode[args[0]], self.intcode[args[1]]
        elif m == '11':
            return args[0], args[1]
        elif m == '10':
            return self.intcode[args[0]], args[1]
        elif m == '01':
            return args[0], self.intcode[args[1]]
        else:
            raise RuntimeError

    def exec(self, opcode, modes, args):
        # which operation?
        if opcode == '01':
            x, y = self.parse_modes(modes, args)
            self.intcode[args[-1]] = x + y
            return True
        elif opcode == '02':
            x, y = self.parse_modes(modes, args)
            self.intcode[args[-1]] = x * y
            return True
        elif opcode == '03':
            self.intcode[args[-1]] = self.input
            return True
        elif opcode == '04':
            print(f'Value at address {args[-1]} is {self.intcode[args[-1]]}')
            return True
        elif opcode == '99':
            return False
        else:
            raise RuntimeError

    def read(self, inst):
        opcode_dict = {"99": 0, "01": 3, "02": 3, "03": 1, "04": 1} # how many args each instruction takes
        opcode = f'{inst:05d}'
        return (opcode[-2:], opcode[:-2], opcode_dict[opcode[-2:]])

    # Differences from day 2:
    #  - opcode is a string of length 5, padded with 0 if necessary
    #  - args are NOT always of length 4
    def process(self):
        status = True
        while status and self.idx < len(self.intcode):
            opcode, modes, nargs = self.read(self.intcode[self.idx]) # read current instruction to determine opcode, args, and parameter modes
            args = self.intcode[self.idx + 1:self.idx + nargs + 1]
            #print(opcode, modes, nargs, args)
            status = self.exec(opcode, modes, args)
            self.output = self.intcode[0]
            self.idx += nargs + 1

if __name__ == '__main__':
    input_value = int(input("Enter the input instruction >>> "))

    intcode_str = read_file('5.input')[0].split(',')

    intcode = Intcode(intcode_str, input_value)

    print("======= Intcode Diagnostic Run =======")
    intcode.process()

    print("======== Part 2 ========")
