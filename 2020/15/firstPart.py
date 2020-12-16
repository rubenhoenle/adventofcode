#!/usr/bin/python3

def findPositions(elements, value):
    index_pos_list = [i for i in range(len(elements)) if elements[i] == value]
    return index_pos_list

lines = []

f = open('data.txt')
for line in f.readlines():
    lines.append(line)
f.close()

start_numbers = []

for word in lines[0].split(','):
    start_numbers.append(int(word))

turns = []
turns.insert(0, -1)

for i in range(len(start_numbers)):
    turns.insert(i+1, start_numbers[i])

for t in range(i+1, 2020):
    last_spoken = turns[len(turns) - 1]
    indexes = findPositions(turns, last_spoken)
    if not indexes:
        turns.insert(t+1, 0)
    elif (len(indexes) == 1):
        turns.insert(t+1, 0)
    else:
        assert(len(indexes) >= 2)
        last = indexes[len(indexes) - 1]
        secondlast = indexes[len(indexes) - 2]
        turns.insert(t+1, last-secondlast)

print('2020th number spoken is', turns[2020])
