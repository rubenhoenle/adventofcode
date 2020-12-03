#!/usr/bin/python3

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

lengthDown = len(lines)
lengthRight = len(lines[0])

stepDown = [1, 1, 1, 1, 2]
stepRight = [1, 3, 5, 7, 1]

result = 1

for x in range(len(stepRight)):
	down = 0
	right = 0
	numberOfTrees = 0

	while (down < lengthDown):
		if(right >= lengthRight):
			right = right - lengthRight
		if(lines[down][right] == '#'):
			numberOfTrees = numberOfTrees + 1	
		right = right + stepRight[x]
		down = down + stepDown[x]
	print('Number of trees: ' + str(numberOfTrees))
	result = result * numberOfTrees

print('result is ' + str(result))
