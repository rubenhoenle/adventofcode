#!/usr/bin/python3

from aoctools import InputReader

input = InputReader.strings('./input/06.txt')[0]

def get_marker_pos(input: str, blocksize: int):
    for i in range(blocksize - 1, len(input)):
        block = input[i-blocksize+1 : i+1]
        if len(set(block)) == len(block):
            return i+1

print('Part 1:', get_marker_pos(input, 4))
print('Part 2:', get_marker_pos(input, 14))
