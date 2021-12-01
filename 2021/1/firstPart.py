#!/usr/bin/python3

numbers = []

with open("input.txt") as inputFile:
    numbers = list(map(int, inputFile.readlines()))

count = 0
for i in range(1, len(numbers)):
    if(numbers[i] > numbers[i-1]):
        count += 1

print(count)