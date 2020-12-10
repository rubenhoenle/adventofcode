#!/usr/bin/python3

import math

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(int(line))
f.close()

fuels = []

def calcFuels(mass):
    return (math.floor(mass / 3) - 2)

for line in lines:
    add = line
    value = 0 - add
    while (add >= 0):
        value += add
        add = calcFuels(add)
    fuels.append(value)

sum = 0
for fuel in fuels:
    sum += fuel

print(sum)