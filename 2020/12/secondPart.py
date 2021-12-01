#!/usr/bin/python3

import math

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

east = 0
north = 0

wp_east = 10
wp_north = 1

directions = ['N', 'E', 'S', 'W']

#    N
# W     E
#    S

for line in lines:
    direction = line[0]
    value = int(line[1:])

    if(direction == 'F'):
        north += value * wp_north
        east += value * wp_east
    elif(direction == 'L'):
        if(value = 90):
            old_wp_north = wp_north
            old_wp_east = wp_east
            wp_north = (old_wp_north * math.cos(math.pi / 2)) - (wp_east * math.sin(math.pi / 2))
        elif(value == 180):
            wp_north = wp_north * (-1)
            wp_east = wp_east * (-1)
        elif(value == 270):
    elif(direction == 'R'):
        if(value = 90):
            
        elif(value == 180):
            wp_north = wp_north * (-1)
            wp_east = wp_east * (-1)
        elif(value == 270):

    elif(direction == 'N'):
        wp_north += value
    elif(direction == 'S'):
        wp_north -= value
    elif(direction == 'E'):
        wp_east += value
    elif(direction == 'W'):
        wp_east -= value
    else:
        print('error')
        quit()

if (north < 0):
    north = north * (-1)
if (east < 0):
    east = east * (-1)

print(north, ' + ', east, ' = ', north + east)