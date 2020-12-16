#!/usr/bin/python3

def findPositions(elements, value):
    try:
        index = len(elements) - 1 - elements[::-1].index(value)
    except ValueError:
        index = -1
    return index

lines = []

f = open('data.txt')
for line in f.readlines():
    lines.append(line)
f.close()

start_numbers = []

for word in lines[0].split(','):
    start_numbers.append(int(word))

def game(start_numbers, count):
    turns = []
    turns.insert(0, -1)
    for i in range(len(start_numbers)):
        turns.insert(i+1, start_numbers[i])

    for t in range(i+1, count):
        last_spoken = turns[len(turns) - 1]
        temp = turns[:]
        temp.pop()
        index = findPositions(temp, last_spoken)
        if(index == -1):
            turns.insert(t+1, 0)
        else:
            turns.insert(t+1, t - index)
    return turns[count]

print('30000000th number spoken is', game(start_numbers, 30000000))
