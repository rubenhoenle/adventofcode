#!/usr/bin/python3

from aoctools import InputReader

lines = InputReader.strings("./input/2.txt")

horizontalPosition = 0
depth = 0

for line in lines:
    direction = line.split(' ')[0]
    value = int(line.split(' ')[1])

    if(direction == "forward"):
        horizontalPosition += value

    elif(direction == "down"):
        depth += value

    elif(direction == "up"):
        depth -= value

print(horizontalPosition * depth)
