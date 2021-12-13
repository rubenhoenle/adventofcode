#!/usr/bin/python3

from aoctools import InputReader, Part
import re

def remove_duplicates(list_with_duplicates: list):
    result = []
    for x in list_with_duplicates: 
        if x not in result: result.append(x)
    return result

def print_coordinates(map: list):
    x_arr: list = ['.'] * (max([x[0] for x in map]) + 1)
    y_arr = [x_arr.copy() for i in range(0, max([y[1] for y in map]) + 1)]
    for coordinate in map: y_arr[coordinate[1]][coordinate[0]] = '#'
    for line in y_arr: print(''.join(l for l in line))

def fold_paper(instructs: list, coords: list, part: Part):
    for instruction in instructs:
        middle = int(re.findall('\d+', instruction)[0])
        t = 1 if 'y' in instruction else 0
        for i in range(len(coords)):
            if coords[i][t] > middle: coords[i][t] -= (coords[i][t] - middle) * 2
        coords = remove_duplicates(coords)

        # for part 1 only execute the first folding instruction
        if(part == Part.ONE): break
    return coords

# get the input and parse it
input = InputReader.strings('./input/13.txt')
coordinates = [list(map(int, i.split(','))) for i in input if re.match('\d+,\d+', i)]
fold_intructions = [i for i in input if re.match('fold along (x|y)=\d+', i)]

# fold the paper and print the results
print("Part 1: " + str(len(fold_paper(fold_intructions, coordinates, Part.ONE)))) # 755
print_coordinates(fold_paper(fold_intructions, coordinates, Part.TWO)) # BLKJRBAG