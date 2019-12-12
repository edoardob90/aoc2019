#!/usr/bin/env python3
def get_fuel(x):
    return (int(x) // 3) - 2

with open("input.dat", "r") as modules:
    total_fuel = 0
    for m in modules:
        module_fuel = 0
        while (get_fuel(m) > 0):
            m = get_fuel(m)
            module_fuel += m
        total_fuel += module_fuel
    print(f"Total fuel needed: {total_fuel}")
