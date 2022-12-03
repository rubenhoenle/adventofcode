#!/usr/bin/python3

from aoctools import InputReader

def findCommonItem(first: str, second: str, third: str = 'DEFAULT'):
    if third == 'DEFAULT': third = second
    for item in first:
        if item in second and item in third:
            return item

def calcItemPriority(item: str):
    incr = 0 if item.islower() else 26
    return [ord(char) - 96 for char in item.lower()][0] + (0 if item.islower() else 26)

input = InputReader.strings('./input/03.txt')

# part 1
sum = 0
for line in input:
    firstcompartment, secondcompartment = line[:len(line)//2], line[len(line)//2:]
    item = findCommonItem(firstcompartment, secondcompartment)
    sum += calcItemPriority(item)
print('Part 1:', sum)

# part 2
sum = 0
i = 0
while i < len(input) - 2:
    item = findCommonItem(input[i], input[i+1], input[i+2])
    sum += calcItemPriority(item)
    i += 3

print('Part 2:', sum)
    