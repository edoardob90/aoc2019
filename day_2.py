#!/usr/bin/env python3
"""
Template for Python solution
"""

from aocd import submit
import fileinput
import sys

class Intcode():
    def __init__(self, init):
        if not isinstance(init, list):
            raise TypeError
        self.intcode = [int(x) for x in init]
        self.idx = 0 # instruction pointer

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

    def jump(self, args):
        assert len(args) >= 0, "Step must be non-negative"
        self.idx += len(args)

    def exec(self, args):
        assert len(args) == 4, "Instructions length must be 4"
        opcode, addr = args[0], args[1:]
        if opcode == 1:
            self.intcode[addr[-1]] = self.intcode[addr[0]] + self.intcode[addr[1]]
            return True
        elif opcode == 2:
            self.intcode[addr[-1]] = self.intcode[addr[0]] * self.intcode[addr[1]]
            return True
        elif opcode == 99:
            return False
        else:
            raise RuntimeError

    def process(self):
        status = True
        while status and self.idx < len(self.intcode):
            args = self.intcode[self.idx:self.idx + 4] # instruction arguments: 1 opcode + 3 parameters
            status = self.exec(args)
            self.output = self.intcode[0]
            self.jump(args)

if __name__ == '__main__':
    intcode_str = fileinput.input().readline().split(',')
    intcode = Intcode(intcode_str)
    #intcode = [int(x) for x in fileinput.input().readline().split(',')]

    # Part 1
    intcode[1] = 12 # the "noun"
    intcode[2] = 2 # the "verb"

    print("=======\nPart 1\n=======")
    print(intcode)
    intcode.process()
    print(intcode.output)

    # Part 2
    print("========\nPart 2\n========")

    for noun in range(100):
        for verb in range(100):
            intcode.reset(intcode_str, noun, verb)
            intcode.process()
            if intcode[0] == 19690720:
                print(intcode[0])
                print(f'Noun: {intcode[1]}\nVerb: {intcode[2]}\nResult: {intcode[1] * 100 + intcode[2]}')
                break


