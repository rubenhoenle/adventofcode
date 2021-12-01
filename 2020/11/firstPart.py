#!/usr/bin/python3

import string
import itertools
adjacent = [(i, j) for i, j in itertools.product(range(-1, 2, 1), repeat=2) if i != 0 or j != 0]

ugly_lines = []

# read the data from the file
f = open('data2.txt')
for line in f.readlines():
	ugly_lines.append(str(line.split('\n')[0]))
f.close()

seats = []
temp = ''
for x in range(len(ugly_lines[0]) + 2):
	temp = temp + '.'

seats.append(temp)
for line in ugly_lines:
	seats.append('.' + line + '.')
seats.append(temp)

def matrix(seats, x, y):
	m = []
	m.append(seats[y - 1][x - 1]  + seats[y - 1][x] + seats[y - 1][x + 1])
	m.append(seats[y][x - 1]  + seats[y][x] + seats[y][x + 1])
	m.append(seats[y + 1][x - 1]  + seats[y + 1][x] + seats[y + 1][x + 1])
	return m

def singleLine(seats, x, y):
	s = ''
	if((x > 0) and (y > 0)):
		s = s + seats[y - 1][x - 1]
	else:
		s = s + '.'
	
	if (y > 0):
		s = s + seats[y - 1][x]
	else:
		s = s + '.'

	if ((y > 0) and (x < len(seats[0]) - 1)):
		s = s + seats[y - 1][x + 1]
	else:
		s = s + '.'

	if (x > 0):
		s = s + seats[y][x - 1]
	else:
		s = s + '.'

	s = s + seats[y][x]

	if (x < len(seats[0]) - 1):
		s = s + seats[y][x + 1]
	else:
		s = s + '.'
	
	if((y < len(seats) - 1) and (x > 0)):
		s = s + seats[y + 1][x - 1]
	else:
		s = s + '.'
	
	if(y < len(seats) - 1):
		s = s + seats[y + 1][x]
	else:
		s = s + '.'
	
	if((y < len(seats) - 1) and (x < len(seats[0]) - 1)):
		s = s + seats[y + 1][x + 1]
	else:
		s = s + '.'

	return s

#nextseats = seats[:]
#while(changed):
def seatcalc(seats):
	length = len(seats[0])
	nextseats = []
	while (nextseats != seats):
		nextseats = seats[:]
		seats = []
		seats.append('............')
		for y in range(1, len(nextseats) - 1):
			row = '.'
			for x in range(1, len(nextseats[y]) - 1):
				if(nextseats[y][x] == '.'):
					row += '.'
				else:
					mtrix = matrix(nextseats[:], x, y)
					s = ''
					for m in mtrix:
						s = s + m
					if(nextseats[y][x] == 'L'):
						if not ('#' in s):
							row += '#'
						else:
							row += 'L'

					elif(nextseats[y][x] == '#'):
						if(s.count('#') >= 4):
							row += 'L'
						else:
							row += '#'

					else:
						print('error')
						quit()
			while(len(row) < length):
				row += '.'
			seats.append(row)
			#print(seats)
		seats.append('............')
	#print(seats)
	return seats

def count_adjacent_seats(row_id, col_id, seats):
    counter = 0
    for off_i, off_j in adjacent:
        if 0 <= row_id + off_i < len(seats) and 0 <= col_id + off_j < len(seats[row_id + off_i]) and seats[row_id+off_i][col_id+off_j] == "#":
            counter += 1
    return counter

print(seats)
seats = seatcalc(seats[:])
print(seats)

for y in range(1, len(seats) - 1):
	for x in range(1, len(seats[y]) - 1):
		print('x ', x, '   y ', y)
		a = count_adjacent_seats(y, x, seats[:])
		ma = matrix(seats[:], x, y)
		s=''
		for m in ma:
			s += m
		b = s.count('#')
		if(a!=b):
			print('error')
			quit()
print('end')

#seats = seatcalc(seats[:])

#for x in range(0, 10):
#print(seats)
seats = seatcalc(seats[:])

# count the number of occupied seats and print it
value = 0
for seat in seats:
	value += seat.count('#')
print(value)