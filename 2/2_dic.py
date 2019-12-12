#!/usr/bin/env python3
import sys

def reset_intcode():
    with open("input.dat", "r") as f:
        return [int(x) for x in f.readline().split(',')]

def set_noun_verb(noun, verb):
    """
    sets the values place in address 1 (noun) and 2 (verb)
    """
    intcode = reset_intcode()
    intcode[1] = noun
    intcode[2] = verb
    return intcode

def process_intcode(intcode):
    """
    idx is the instruction pointer
    code is the current opcode
    each opcode is followed by 1 or more instruction's parameters
    """
    for idx in range(0, len(intcode), 4):
        code = intcode[idx]
        ia = intcode[idx + 1]
        ib = intcode[idx + 2]
        ires = intcode[idx + 3]
        if code == 1:
            intcode[ires] = intcode[ia] + intcode[ib]
        elif code == 2:
            intcode[ires] = intcode[ia] * intcode[ib]
        elif code == 99:
            break
        else:
            print(f"Something went wrong: unrecognized opcode!", file=sys.stderr)
            sys.exit(-1)

    return intcode[0]

for noun in range(100):
    for verb in range(100):
        print(f"Trying with noun = {noun} and verb = {verb}", file=sys.stderr)
        intcode = set_noun_verb(noun, verb)
        res = process_intcode(intcode)
        if res == 19690720:
            print(f"Pair noun and verb = ({noun}, {verb})")
            print(f"Result = {100*noun+verb}")
            sys.exit(0)
