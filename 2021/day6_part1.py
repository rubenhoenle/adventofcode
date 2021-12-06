#!/usr/bin/python3

from inputreader import InputReader

debugging_output = False

# get the input, parse it and (if needed) print the initial state
lanternfishes = list(map(int, InputReader.strings("./input/6.txt")[0].split(",")))
if debugging_output: print("Initial state: " + str(lanternfishes))

# simulate the 80 days
for day in range(0, 80):
    for i in range(0, len(lanternfishes)):
        lanternfishes[i] -= 1
        if lanternfishes[i] < 0:
            lanternfishes[i] = 6
            lanternfishes.append(8)

    # if needed: output the current state
    if debugging_output: print("After " + str(day+1) + " days: " + str(lanternfishes))

# print the result of the simulation
print("Total number of lanternfishes: " + str(len(lanternfishes)))