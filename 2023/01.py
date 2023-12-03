#!/usr/bin/python3

import re
from aoctools import InputReader

input = InputReader.strings('./input/01.txt')

word_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def part1(input):
    sum = 0
    for line in input:
        without_letters = re.sub('[A-Za-z]', '', line)
        sum += int(without_letters[0] + without_letters[-1])
    return sum

def part2(input):
    parsed_lines = []
    for line in input:
        positions = {}
        for key, value in word_to_num.items():
            for match in re.finditer(key + "|" + value, line):
                positions[match.start()] = value
        positions = dict(sorted(positions.items()))
        parsed = ""
        for key, value in positions.items():
            parsed += value
        parsed_lines.append(parsed)
    return parsed_lines

# PART 1
print("Part 1:", part1(input))

# PART 2
result = part2(input)
print("Part 2:", part1(result))

