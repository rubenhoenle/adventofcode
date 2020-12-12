#!/usr/bin/python3

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

facing = 'E'
east = 0
north = 0

directions = ['N', 'E', 'S', 'W']

#    N
# W     E
#    S

for line in lines:
    direction = line[0]
    value = int(line[1:])

    if(direction == 'F'):
        direction = facing
    elif(direction == 'L'):
        deg = int(value / 90)
        idx = directions.index(facing)
        direction = directions[idx - deg]
        facing = direction
        value = 0

    elif(direction == 'R'):
        deg = int(value / 90)
        idx = directions.index(facing)
        idx += deg
        if(idx>= 3):
            idx -=4
        direction = directions[idx]
        facing = direction
        value = 0

    if(direction == 'N'):
        north += value
    elif(direction == 'S'):
        north -= value
    elif(direction == 'E'):
        east += value
    elif(direction == 'W'):
        east -= value
    else:
        print('error')
        quit()

if (north < 0):
    north = north * (-1)
if (east < 0):
    east = east * (-1)

print(north, ' + ', east, ' = ', north + east)