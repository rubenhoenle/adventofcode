#!/usr/bin/python3

from aoctools import InputReader
import numpy as np

# check if the given point is the lowest between its adjacents
def is_low_point(pointmap, x, y):
    adjacents = []
    if (y > 0): adjacents.append(pointmap[y-1][x]) # look up
    if (y < len(pointmap) - 1): adjacents.append(pointmap[y+1][x]) # look down
    if (x > 0): adjacents.append(pointmap[y][x-1]) # look left
    if (x < len(pointmap[y]) - 1): adjacents.append(pointmap[y][x+1]) # look right
    return len([a for a in adjacents if int(a) <= int(pointmap[y][x])]) == 0

# calculate the basins for part 2
def calc_basin(num: int, pointmap: list, x: int, y: int, up=True, down=True, right=True, left=True):
    look_up = False; look_down = False; look_right = False; look_left = False
    if(x >= 0 and x <= len(pointmap[0]) - 1):
        # look up
        if (up and y > 0 and pointmap[y-1][x] != 9 and not isinstance(pointmap[y-1][x], list)): 
            pointmap[y-1][x] = [pointmap[y-1][x], num]
            look_up = True
        # look down
        if (down and y < len(pointmap) - 1 and pointmap[y+1][x] != 9 and not isinstance(pointmap[y+1][x], list)): 
            pointmap[y+1][x] = [pointmap[y+1][x], num] 
            look_down = True
    if(y >= 0 and y <= len(pointmap) - 1):
        # look left
        if (left and x > 0 and pointmap[y][x-1] != 9 and not isinstance(pointmap[y][x-1], list)): 
            pointmap[y][x-1] = [pointmap[y][x-1], num]
            look_left = True
        # look right
        if (right and x < len(pointmap[y]) - 1 and pointmap[y][x+1] != 9 and not isinstance(pointmap[y][x+1], list)):
            pointmap[y][x+1] = [pointmap[y][x+1], num] 
            look_right = True

    if look_up:     pointmap = calc_basin(num, pointmap, x, y-1, True, False, True, True)
    if look_down:   pointmap = calc_basin(num, pointmap, x, y+1, False, True, True, True)
    if look_left:   pointmap = calc_basin(num, pointmap, x-1, y, True, True, False, True)
    if look_right:  pointmap = calc_basin(num, pointmap, x+1, y, True, True, True, False)
    return pointmap

# get the input and parse it
input = InputReader.strings('./input/9.txt')
heightmap = [[] for x in range(len(input))]
for i in range(0, len(input)):
    for c in [c for c in input[i]]:
        heightmap[i] += [int(c)]

# calculate
num = 0; risk_level = 0
for y in range(0, len(heightmap)):
    for x in range(0, len(heightmap[y])):
        if is_low_point(input, x, y):
            risk_level += 1 + int(input[y][x]) # part 1 
            # part 2
            calc_basin(num, heightmap, x, y)
            heightmap[y][x] = [heightmap[y][x], num]
            num += 1

# parse the result of part 2
result = [[] for x in range(num)]
for line in heightmap: 
    for val in [l for l in line if isinstance(l, list)]: 
        result[val[1]] += [val[0]]
for i in range(0, len(result)): result[i] = len(result[i])

# print the result
print("Part 1: " + str(risk_level)) #631
print("Part 2: " + str(np.prod(-np.sort(-np.array(result))[:3]))) #821560