#!/usr/bin/python3

import re
import numpy as np
from inputreader import InputReader

# add a horizontal or vertical line from the given coordinates to the diagram
def add_horizontal_or_vertical_line(field, x1, x2, y1, y2):
    if(x1 == x2):
        lower_y = y1 if y1 < y2 else y2
        greater_y = y2 + 1 if y1 < y2 else y1 + 1
        for i in range(lower_y, greater_y):
                field[i][x1] += 1
        
    if(y1 == y2):
        lower_x = x1 if x1 < x2 else x2
        greater_x = x2 + 1 if x1 < x2 else x1 + 1
        for i in range(lower_x, greater_x):
                field[y1][i] += 1

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
    add_horizontal_or_vertical_line(diagram, c[0], c[2], c[1], c[3])

# print the result
if(maxValue < 30): print_diagram(diagram)
print("Number of overlaps: " + str(count_overlaps(diagram)))