#!/usr/bin/python3

from aoctools import InputReader

def simulate_flashing(energy_levels: list, flashed_ones: list, x: int, y: int):
    if not energy_levels[y][x] > 9 or flashed_ones[y][x]: return energy_levels, flashed_ones
    flashed_ones[y][x] = True

    if x < len(energy_levels[0]) - 1:
        octopus_energy_levels[y][x+1] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x+1, y)

    if x < len(energy_levels[0]) - 1 and y > 0:
        octopus_energy_levels[y-1][x+1] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x+1, y-1)

    if x < len(energy_levels[0]) - 1 and y < len(energy_levels) - 1:
        octopus_energy_levels[y+1][x+1] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x+1, y+1)

    if x > 0:
        octopus_energy_levels[y][x-1] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x-1, y)

    if x > 0 and y > 0:
        octopus_energy_levels[y-1][x-1] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x-1, y-1)
    
    if x > 0 and y < len(energy_levels) -1:
        octopus_energy_levels[y+1][x-1] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x-1, y+1)

    if y > 0:
        octopus_energy_levels[y-1][x] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x, y-1)
    
    if y < len(energy_levels) -1:
        octopus_energy_levels[y+1][x] += 1
        energy_levels, flashed_ones = simulate_flashing(energy_levels, flashed_ones, x, y+1)

    return energy_levels, flashed_ones

# part 2: checks if all octopusses have flashed in the last step
def part2(energy_levels):
    for line in energy_levels:
        for level in line:
            if level != 0: return False
    return True

# get the input and parse it
input = InputReader.strings('./input/11.txt')
octopus_energy_levels = [[] for x in range(len(input))]
for i in range(0, len(input)):
    for c in [c for c in input[i]]:
        octopus_energy_levels[i] += [int(c)] 

# simulate the 100 steps
total_flashes = 0; step = 0
while not part2(octopus_energy_levels):
    flashed_octopusses = [[False] * len(octopus_energy_levels[0]) for e in octopus_energy_levels]
    for y in range(0, len(octopus_energy_levels)):
        for x in range(0, len(octopus_energy_levels[y])):
            # first, the energy level of each octopus increases by 1
            octopus_energy_levels[y][x] += 1
            # then, any octopus with an energy level greater than 9 flashes
            octopus_energy_levels, flashed_octopussed = simulate_flashing(octopus_energy_levels, flashed_octopusses, x, y)

    # finally any octopus that flashed during this step has its energy level set to 0
    for y in range(0, len(octopus_energy_levels)):
        for x in range(0, len(octopus_energy_levels[y])):
            if flashed_octopusses[y][x]:
                # count the total flashes of the first 100 steps for part 1
                if step < 100: total_flashes += 1
                # set the energy level to 0
                octopus_energy_levels[y][x] = 0
    step += 1

print("Part 1: " + str(total_flashes)) # 1681
print("Part 2: " + str(step)) # 276