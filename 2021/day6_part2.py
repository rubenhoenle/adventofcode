#!/usr/bin/python3

from aoctools import InputReader

debugging_output = False

# get the input, parse it and (if needed) print the initial state
input = list(map(int, InputReader.strings("./input/6.txt")[0].split(",")))
if debugging_output: print("Initial state: " + str(input))

# set up an array to count how many lanternfishes are in which state
lanternfishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for value in input:
    lanternfishes[value] += 1
if debugging_output: print("              " + str(lanternfishes))

# simulate the 256 days
for day in range(0, 256):
    temp = 0
    number_of_fishes_state_zero = lanternfishes[0]
    for i in range(len(lanternfishes)-1, -1, -1):
        temp2 = temp
        temp = lanternfishes[i]
        lanternfishes[i] = temp2
        if i == 0:
            lanternfishes[6] += number_of_fishes_state_zero
            lanternfishes[8] += number_of_fishes_state_zero

    # if needed: output the current state
    if debugging_output: print("After " + str(day+1) + " days: " + str(lanternfishes))

# print the result of the simulation
print("Total number of lanternfishes: " + str(sum(lanternfishes)))