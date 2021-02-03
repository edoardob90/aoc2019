#!/usr/bin/env python3
"""
Template for Python solution
"""

import fileinput
from sys import exit
from aoc import timer
from collections import defaultdict

def mandist(p1, p2=[0,0]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#class Vector:
#    def __init__(self, data):
#        self.data = data
#
#    def __repr__(self):
#        return f'{self.data}'
#
#    def __add__(self, other):
#        data = []
#        for j in range(len(self.data)):
#            data.append(self.data[j] + other.data[j])
#        return Vector(data)
#
#    def __sub__(self, other):
#        data = []
#        for j in range(len(self.data)):
#            data.append(self.data[j] - other.data[j])
#        return Vector(data)
#
#    def as_tuple(self):
#        return tuple(self.data)

class Path:
    def __init__(self, init, start=[0,0], end=[0,0]):
        if not isinstance(init, list):
            raise TypeError
        self.path = [(x[0], int(x[1:])) for x in init]
        self.points = set()
        self.distances = defaultdict(int)

    def __repr__(self):
        return f'Path: {self.path}\nstart = {self.start} end = {self.end}\nPoints:\n{self.points}\n'

    def follow(self):
        x, y = 0, 0
        distance = 0
        for p in self.path:
            assert p[0] in ['R','L','D','U']
            for _ in range(p[1]):
                if   p[0] == 'R':
                    x += 1
                elif p[0] == 'L':
                    x -= 1
                elif p[0] == 'U':
                    y += 1
                elif p[0] == 'D':
                    y -= 1

                # add current point to the path
                self.points.add((x, y))

                # accumulate distance
                distance += 1
                self.distances[(x, y)] = distance

        return self.points

    def crossing_distance(self, crossings):
        return {p: self.distances[p] for p in self.points if p in crossings}

if __name__ == '__main__':
    lines = [*fileinput.input()]
    paths = [Path(x.split(',')) for x in lines]

    p1 = paths[0].follow()
    p2 = paths[1].follow()
    crossings = p1 & p2
    dist = min(mandist(p) for p in crossings)
    print('======= Part 1 =======')
    #print(f'{p1}\n{p2}')
    #print(crossings)
    print(f'Distance to the closest crossing: {dist}')

    print('======= Part 2 =======')
    cd1 = paths[0].crossing_distance(crossings)
    cd2 = paths[1].crossing_distance(crossings)
    dist2 = min(cd1[i] + cd2[i] for i in crossings)
    print(f'Fewest combined steps: {dist2}')
