#!/usr/bin/python3

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

lengthDown = len(lines)
lengthRight = len(lines[0])

down = 0
right = 0
numberOfTrees = 0

while (down < lengthDown):
	if(right >= lengthRight):
		right = right - lengthRight
	if(lines[down][right] == '#'):
		numberOfTrees = numberOfTrees + 1	
	right = right + 3
	down = down + 1

print('Number of trees: ' + str(numberOfTrees))
