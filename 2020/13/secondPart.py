#!/usr/bin/python3

lines = []

f = open('data2.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

earliest = int(lines[0])

busses = []
for word in lines[1].split(','):
    if(word != 'x'):
        busses.append(int(word))

timestamps = []
for t in range(earliest, earliest + 100):
    timestamps.append(t)

t = 0
next = busses[0]
for timestamp in timestamps:
    for i in range(len(busses)):
        if(timestamp % busses[i] == 0):
            if(i == 0):
                t = timestamp
            if(i + 1 < len(busses)):
                nt = 0
                for temp in range(timestamp, timestamps[len(timestamps) - 1]):
                    if(temp % busses[i+1] == 0):
                        nt = temp
                        break
                assert(nt != 0)
                if(busses[i] + timestamp < nt):
                    break
            else:
                print('solution: ', t)
                
            #if (busses[i] == next):
            #    if(i+1 >= len(busses)):
            #        print('Solution is:', t)
            #        quit()
            #    next = busses[i+1]
            #    if(t == 0):
            #        t = timestamp
            #else: 
            #    next = busses[0]
            #   #i -= 1
            #  t = 0
            # break

