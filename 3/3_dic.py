#!/usr/bin/env python3
import sys
from operator import add
import numpy as np

def make_move(move_str, point):
    step = int(move_str[1])
    dir = move_str[0]
    if dir == "R":
        point[0] += step
    elif dir == "L":
        point[0] -= step
    elif dir == "U":
        point[1] += step
    elif dir == "D":
        point[1] -= step
    else:
        raise RuntimeError("Unrecognized move type!")

    return point

def cb_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

distance = 0
x = [int(x) for x in list(input("Initial point? ").split(','))]
move_str = input("Move string? ")

for move in move_str.strip().split(','):
    y = x.copy()
    x = make_move(move, x)
    distance += cb_dist(x, y)
    print(f"Point = {tuple(x)} and distance = {distance}")


print(f"\nFinal point = {tuple(x)}\nTotal city-block distance = {distance}")
