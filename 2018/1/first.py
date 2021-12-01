#!/usr/bin/python3

f = open('input.txt', 'r')

lines = f.readlines()

numbers = []
for line in lines:
	numbers.append(int(line))

i = 0
for number in numbers:
	i = i + number

print(i)
