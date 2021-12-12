#!/usr/bin/python3

from aoctools import InputReader
import re

def find_paths(map, current, end, visit_single_small_cave_twice):
    last_curr = current.split(',')[-2]; paths = []
    for line in [m for m in map if last_curr in m]:
        curr = current; visit_twice = visit_single_small_cave_twice
        matches = re.findall('(\w+)-(\w+)', line)[0]
        if matches[0] == last_curr: i = 1
        elif matches[1] == last_curr: i = 0
        else: continue

        if ((matches[i] == 'start') or (not visit_twice and str(matches[i]).islower() and matches[i] + ',' in curr)): continue
        if str(matches[i]).islower() and matches[i] + ',' in curr: visit_twice = False
        curr += matches[i] + ','
        
        paths += [curr] if curr.split(',')[-2] == end else find_paths(map, curr, end, visit_twice)
    return paths

# get the input
input = InputReader.strings('./input/12.txt')

# calculate and print the results
print("Part 1: " + str(len(find_paths(input, "start,", "end", False)))) # 3369
print("Part 2: " + str(len(find_paths(input, "start,", "end", True)))) # 85883