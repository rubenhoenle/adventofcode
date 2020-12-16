#!/usr/bin/python3

def game(start_numbers, count):
    turns = []
    for i in range(len(start_numbers)):
        turns.append(start_numbers[i])

    turn_dict = {turn: counter + 1 for counter, turn in enumerate(turns[:-1])}
    last = turns[len(turns) - 1]
    for t in range(len(turns), count):
        n = 0
        if (last in turn_dict):
            n = t - turn_dict[last]
        turn_dict[last] = t
        last = n
    return last

lines = []
f = open('data.txt')
for line in f.readlines():
    lines.append(line)
f.close()

start_numbers = []
for word in lines[0].split(','):
    start_numbers.append(int(word))

print('30000000th number spoken is', game(start_numbers, 30000000))
