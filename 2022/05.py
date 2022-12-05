#!/usr/bin/python3

import re, copy
from aoctools import InputReader

input = InputReader.strings('./input/05.txt')

numberOfStacks = [line for line in input if line.startswith(' 1   2   3')][0]
numberOfStacks = int(numberOfStacks.split()[-1])

stacks = [[] for _ in range(numberOfStacks)]
stackLines = [line for line in input if '[' in line]
stackLines.reverse()
for line in stackLines:
    i = 1
    while i < len(line):
        if(line[i] != ' '):
            stacks[int((i-1) / 4)].append(line[i])
        i += 4

stackCopy = copy.deepcopy(stacks)

# part 1
for line in [line for line in input if line.startswith('move')]:
    step = [int(i) for i in re.split('move (\d+) from (\d+) to (\d+)', line)[1:4]]
    for i in range(0, step[0]):
        stacks[step[2]-1].append(stacks[step[1]-1].pop())

print('Part 1:', ''.join([arr[-1] for arr in stacks])) # PSNRGBTFT

# part 2
stacks = stackCopy
for line in [line for line in input if line.startswith('move')]:
    step = [int(i) for i in re.split('move (\d+) from (\d+) to (\d+)', line)[1:4]]
    poppeditems = []
    for i in range(0, step[0]):
        poppeditems.append(stacks[step[1]-1].pop())
    poppeditems.reverse()
    stacks[step[2]-1] += poppeditems

print('Part 2:', ''.join([arr[-1] for arr in stacks])) # BNTZFPMMW
