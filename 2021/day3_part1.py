#!/usr/bin/python3

from inputreader import InputReader

lines = InputReader.strings("./input/3.txt")

gamma = ""
epsilon = ""

for i in range(0, len(lines[0])):
    ones = 0
    zeros = 0
    for line in lines:
        if(int(line[i])):
            ones += 1
        else:
            zeros += 1

    result_gamma = "1" if ones > zeros else "0"
    result_epsilon = "0" if ones > zeros else "1"
    
    gamma = gamma + result_gamma
    epsilon = epsilon + result_epsilon

print(int(gamma, 2) * int(epsilon, 2))
