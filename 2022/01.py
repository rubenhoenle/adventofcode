#!/usr/bin/python3

from aoctools import InputReader

input = InputReader.strings('./input/01.txt')

# parse the input
calories, arr = [], []
for line in input:
    if len(line) == 0:
        calories.append(arr)
        arr = []
    else:
        arr.append(int(line))
calories.append(arr)

calories = [sum(arr) for arr in calories]

# print result of part 1
print('Part 1: ', max(calories))

# print result of part 2
calories.sort()
print('Part 2: ', sum(calories[-3:]))