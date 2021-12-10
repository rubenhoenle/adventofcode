#!/usr/bin/python3

from aoctools import InputReader

open_characters  = ["(", "[", "{", "<"]
close_characters = [")", "]", "}", ">"]

# removes stuff like (), {}, [], <>
def remove_empty_chunks(lines: list) -> list:
    for i in range(0, len(lines)):
        for pair in ["()", "{}", "[]", "<>"]: lines[i] = lines[i].replace(pair,"")
    if len([l for l in lines if len([ x for x in ["()", "{}", "[]", "<>"] if x in l]) > 0]) > 0:
        lines = remove_empty_chunks(lines)
    return lines

# get the input and parse it
input = remove_empty_chunks(InputReader.strings('./input/10.txt'))

# calculate the score for part 1
score_p1 = 0; scores_p1 = [3, 57, 1197, 25137]; corrupt_line_idxs = []
for line in input:
    for i in range(0, len(line)):
        if line[i] in close_characters:
            score_p1 += scores_p1[close_characters.index(line[i])]
            corrupt_line_idxs.append(input.index(line))
            break

# filter out the corrupt lines -> the remaining ones are the incomplete lines
input = [l for l in input if input.index(l) not in corrupt_line_idxs]

# find out which closing chars have to be appended to the incomplete lines
appendix = [""] * len(input)
for i in range(len(input)):
    for c in input[i]: appendix[i] = close_characters[open_characters.index(c)] + appendix[i]

# calculate the score for part 2
score_results_p2 = [0] * len(appendix)
for i in range(0, len(appendix)): 
    for c in appendix[i]: score_results_p2[i] = (score_results_p2[i] * 5) + close_characters.index(c) + 1
score_results_p2.sort() # sort the array

# print the results of both parts
print("Part 1: " + str(score_p1)) # 392043
print("Part 2: " + str(score_results_p2[int(len(score_results_p2) / 2)])) # 1605968119