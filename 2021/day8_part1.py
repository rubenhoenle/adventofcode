#!/usr/bin/python3

from aoctools import InputReader

class Digit: ONE = 2; FOUR = 4; SEVEN = 3; EIGHT = 7

# get the input and parse it
output_values = []
for line in [line.split('|')[1] for line in InputReader.strings('./input/8.txt')]:
    output_values += [l for l in line.split(' ') if l]

# calculate and print the result
output = len([v for v in output_values if len(v) in [Digit.ONE, Digit.FOUR, Digit.SEVEN, Digit.EIGHT]])
print('The digits 1, 4, 7, or 8 appear ' + str(output) + ' times in the output values.') 