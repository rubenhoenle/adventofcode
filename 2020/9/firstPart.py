#!/usr/bin/python3

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

preamble_length = 25

def check(data, index):
    number = int(data[index])
    listA = []
    listB = []
    for x in range(index - preamble_length, index):
        listA.append(int(data[x]))
        listB.append(int(data[x]))

    for a in listA:
        for b in listB:
            if((a+b == number) and (a != b)):
                return False
    return True

for x in range(preamble_length, len(lines)):
    value = check(lines, x)
    if(value):
        print(lines[x])
        break