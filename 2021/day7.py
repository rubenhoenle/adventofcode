#!/usr/bin/python3

from aoctools import InputReader, Part

# calculate the fuel consumption for part 2
def calc_increasing_consumption(start: int, end: int):
    n = abs(start - end)
    return int(((n * n) + n) / 2)

# calculate the fuel consumtion for part 1 OR part 2
def calc_consumption(crab_positions: list, part: Part):
    fuel_consumption= []
    for i in range(0, max(crab_positions) + 1):
        fuel_consumption.append(0)
        for crab in crab_positions:
            fuel_consumption[i] += abs(crab - i) if part == Part.ONE else calc_increasing_consumption(crab, i)
    return fuel_consumption

# prints the result of the fuel consumption calculation
def print_result(fuel_consumption: list, part: Part):
    min_value = min(fuel_consumption)
    position = str(fuel_consumption.index(min_value))
    print("Part " + str(part.value) + ": Minimal fuel consumption is " + str(min_value) + " at horizontal position " + position + ".")

# get the input
crab_positions = InputReader.integers_in_first_line("./input/7.txt")

# print the result
print_result(calc_consumption(crab_positions, Part.ONE), Part.ONE)
print_result(calc_consumption(crab_positions, Part.TWO), Part.TWO)