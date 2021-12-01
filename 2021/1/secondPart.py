#!/usr/bin/python3

numbers = []

with open("input.txt") as inputFile:
    numbers = list(map(int, inputFile.readlines()))

count = 0
windows = []

for i in range(0, len(numbers)-2):
    windows.append(numbers[i] + numbers[i+1] + numbers[i+2])

for i in range(1, len(windows)):
    if(windows[i] > windows[i-1]):
        count += 1

print(count)