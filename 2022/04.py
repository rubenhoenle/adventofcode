#!/usr/bin/python3

import re
from aoctools import InputReader

input = InputReader.strings('./input/04.txt')

part1, part2 = 0, 0
for line in input:
    matches = [int(match) for match in re.split('(\d*)-(\d*),(\d*)-(\d*)', line)[1:5]]
    range1, range2 = list(range(matches[0], matches[1]+1)), list(range(matches[2], matches[3]+1))

    # part 1
    if set(range1).issubset(set(range2)) or set(range2).issubset(set(range1)): part1 += 1

    # part 2
    for i in range1:
        if i in range2:
            part2 += 1
            break

print('Part 1:', part1)
print('Part 2:', part2)