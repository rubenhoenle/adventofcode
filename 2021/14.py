#!/usr/bin/python3
from aoctools import InputReader, Part
import re

# get the input and parse it
input = InputReader.strings('./input/14.txt')
template = input[0]
rules = [re.findall('[A-Z]+', i) for i in input if re.match('[A-Z]{2} -> [A-Z]', i)]

for part in [Part.ONE, Part.TWO]:
    # create the pairs from the template
    pairs = dict.fromkeys([r[0] for r in rules], 0)
    for i in range(0, len(template) -1): pairs[template[i] + template[i+1]] += 1

    # count the occurences of the chars in the template
    count = dict.fromkeys(template,0)
    for c in count: count[c] = template.count(c)

    # iterate over 10 steps for part 1 and 40 for part 2
    for step in range(0, 10 if part == Part.ONE else 40):
        new_pairs = dict.fromkeys([r[0] for r in rules], 0)

        for pair in pairs:
            # get the char which should be inserted
            new_char = rules[[r[0] for r in rules].index(pair)][1]

            # add the char which should be inserted to the dict
            try: count[new_char] += pairs.get(pair)
            except KeyError: count[new_char] = pairs.get(pair)

            # create the new pairs with the insertion char
            new_pairs[pair[0] + new_char] += pairs.get(pair)
            new_pairs[new_char + pair[1]] += pairs.get(pair)

        pairs = new_pairs

    key_max = max(count.keys(), key=(lambda k: count[k]))
    key_min = min(count.keys(), key=(lambda k: count[k]))

    # Part 1: 3587; Part 2: 3906445077999
    print('Part ' + str(part.value) + ': ' + str(count[key_max] - count[key_min]))