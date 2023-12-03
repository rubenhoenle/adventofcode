#!/usr/bin/python3

import re
from aoctools import InputReader

games = [line.split(":")[1].strip() for line in InputReader.strings('./input/02.txt')]

# part 1
def play_game(game: str):
    for subset in [s.strip() for s in game.split(";")]:
        cube_count = { "red": 0, "green": 0, "blue": 0 }
        for color in [c.strip() for c in subset.split(",")]:
            count = int(color.split(" ")[0])
            cube_count[color.split(" ")[1]] = count
        if not(cube_count["red"] <= 12 and cube_count["green"] <= 13 and cube_count["blue"] <= 14):
            return False
    return True

# part 2
def get_min_cubes(game: str):
    cube_count = { "red": [], "green": [], "blue": [] }
    for subset in [s.strip() for s in game.split(";")]: 
        for color in [c.strip() for c in subset.split(",")]:
            count = int(color.split(" ")[0])
            cube_count[color.split(" ")[1]].append(count)
    return max(cube_count["red"]) * max(cube_count["green"]) * max(cube_count["blue"])

part1, part2 = 0, 0
for i in range(0, len(games)):
    if play_game(games[i]):
        part1 += i+1
    
    part2 += get_min_cubes(games[i])

print("Part 1:", part1)
print("Part 2:", part2)
