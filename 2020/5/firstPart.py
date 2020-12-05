#!/usr/bin/python3

import numpy

def getSeatID(row, column):
	seatID = (row * 8) + column
	return seatID

def getRow(row):
	min = 0
	max = 127
	for c in row:
		range = max + 1 - min
		# lower half
		if(c == 'F'):
			min = min
			max = max - int(range / 2)
		# upper half
		elif(c == 'B'):
			max = max
			min = min + int(range / 2)
		else:
			return -1
	rownumber = min
	return rownumber


def getColumn(column):
	min = 0
	max = 7
	for c in column:
		range = max + 1 - min
		# lower half
		if(c == 'L'):
			min = min
			max = max - int(range / 2)
		# upper half
		elif(c == 'R'):
			max = max
			min = min + int(range / 2)
		else:
			return -1
	rownumber = min
	return rownumber


lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

rows = []
columns = []

for line in lines:
	rows.append(line[0:7])
	columns.append(line[-3:])

seatIDs = []

for x in range(len(rows)):
	row = int(getRow(rows[x]))
	column = int(getColumn(columns[x]))
	seatIDs.append(getSeatID(row, column))

max_value = numpy.max(seatIDs)

print('Highest Seat ID is ' + str(max_value))