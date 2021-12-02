#!/usr/bin/python3

from inputreader import InputReader

lines = InputReader.strings("./input/2.txt")

horizontalPosition = 0
depth = 0
aim = 0

for line in lines:
    direction = line.split(' ')[0]
    value = int(line.split(' ')[1])

    if(direction == "forward"):
        horizontalPosition += value
        depth += value * aim

    elif(direction == "down"):
        aim += value

    elif(direction == "up"):
        aim -= value

print(horizontalPosition * depth)
