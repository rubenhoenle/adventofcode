#!/usr/bin/python3

import math

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(int(line))
f.close()

fuels = []
for line in lines:
    value = math.floor(line / 3) - 2
    fuels.append(value)

sum = 0
for fuel in fuels:
    sum += fuel

print(sum)