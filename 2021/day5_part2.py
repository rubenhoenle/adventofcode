#!/usr/bin/python3

import re
import numpy as np
from inputreader import InputReader

# add a line from the given coordinates to the diagram
def add_line(field, x1, x2, y1, y2):
    dx =  abs(x2-x1)
    sx =  1 if x1<x2 else -1
    dy = -abs(y2-y1)
    sy = 1 if y1<y2 else -1
    err = dx+dy 
    while (True):
        field[y1][x1] += 1
        if (x1 == x2 and y1 == y2): break
        e2 = 2*err
        if (e2 >= dy):
            err += dy
            x1 += sx
        if (e2 <= dx):
            err += dx
            y1 += sy


# call to print the diagram
def print_diagram(diagram):
    for d in diagram:
        output = ""
        for i in d: output += "." if i == 0 else str(i)
        print(output)

def count_overlaps(diagram):
    overlaps = 0
    for d in diagram:
        for i in d: overlaps += 1 if i > 1 else 0
    return overlaps

# get the input from the file
lines = InputReader.strings("./input/5.txt")

# parse the input
coordinates = []
for line in lines:
    coordinates.append(list((map(int, re.findall("(\d+),(\d+) -> (\d+),(\d+)", line)[0]))))

# create an empty diagram
maxValue = np.max(coordinates) + 1
diagram = [[ None for y in range(maxValue)] for x in range(np.max(maxValue))]
for t in range(0, len(diagram)):
    for s in range(0, len(diagram[t])):
        diagram[t][s] = 0

# add lines to the diagram
for c in coordinates:
    add_line(diagram, c[0], c[2], c[1], c[3])

# print the result
if(maxValue < 30): print_diagram(diagram)
print("Number of overlaps: " + str(count_overlaps(diagram)))