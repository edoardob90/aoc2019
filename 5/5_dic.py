#!/usr/bin/env python3
import sys

class Intcode():
    def __init__(self):
        self.file = ''
        self.intcode = []
        self.status = "init"

    def __str__(self):
        return (f"Intcode status is currently '{self.status}'")

    def process(self):
        """
        idx: instruction pointer
        code: current opcode
              each opecode is followed by 1 or more instruction's parameters
        """
        for idx in range(0, len(self.intcode), 4):
            code = self.intcode[idx]
            ia = self.intcode[idx + 1]
            ib = self.intcode[idx + 2]
            ires = self.intcode[idx + 3]
            if code == 1:
                self.intcode[ires] = self.intcode[ia] + self.intcode[ib]
            elif code == 2:
                self.intcode[ires] = self.intcode[ia] * self.intcode[ib]
            elif code == 3:
                self.intcode[idx + 1] = int(input("Input value requested >>> "))
            elif code == 99:
                break
            else:
                print(f"Something went wrong: unrecognized opcode!", file=sys.stderr)
                sys.exit(-1)

    def reset(self, filename):
        try:
            with open(filename, 'r') as f:
                self.intcode = [int(x) for x in f.readline().split(',')]
                self.status = "reset"
            self.file = filename
        except FileNotFoundError:
            raise

    def set(self, noun, verb):
        # we first have to reset the intcode
        if (self.status != "reset"):
            print(f"You first have to reset the Intcode before setting a new noun/verb")
            return
        else:
            self.status = "set"
            self.intcode[1] = noun
            self.intcode[2] = verb


# Initialize
intcode = Intcode()
print(intcode)

# Reset (read from input)
intcode.reset('input.dat')
print(intcode)
