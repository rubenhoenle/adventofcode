#!/usr/bin/python3

from aoctools import InputReader

lines = InputReader.strings("./input/3.txt")

# returns how many ones and zeros there are
def count(lines, idx):
    ones = 0
    zeros = 0
    for line in lines:
        if(int(line[idx])):
            ones += 1
        else:
            zeros += 1
    return ones, zeros

# calculates the oxygen generator rating or the co2 srubber rating
def calc(lines, oxygen_rate: bool):
    for i in range(0, len(lines[0])):
        # if there is only one value left, break
        if len(lines) < 2:
            break 

        # count how many ones and zeros there are
        ones, zeros = count(lines, i)

        # check which value is the most common one
        if(oxygen_rate):
            drop = "0" if zeros > ones else "1"
        else:
            drop = "1" if zeros > ones else "0"
        
        # drop the not needed lines
        lines = [l for l in lines if l[i] == drop]
    return lines[0]

oxygenGeneratorRating = calc(lines, True)
co2SrubberRating = calc(lines, False)

print(int(oxygenGeneratorRating, 2) * int(co2SrubberRating, 2))
