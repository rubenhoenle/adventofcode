#!/usr/bin/python3

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

earliest = int(lines[0])

busses = []
for word in lines[1].split(','):
    if(word != 'x'):
        busses.append(int(word))

timestamps = []
for t in range(earliest, earliest + 1000):
    timestamps.append(t)

delay = 0
bus_id = 0

stop = False
for timestamp in timestamps:
    for bus in busses:
        if(timestamp % bus == 0):
            delay = timestamp - earliest
            bus_id = bus
            stop = True
            break
    if(stop):
        break

print('Earliest timestamp where you could leave is: ', earliest)
print('The bus ID you take: ', bus_id)
print('The time you have to wait for the bus: ', delay)
print('Solution is:', delay * bus_id)