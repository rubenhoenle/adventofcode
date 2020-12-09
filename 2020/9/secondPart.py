#!/usr/bin/python3

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(int(str(line.split('\n')[0])))
f.close()

preamble_length = 25

def check(data, index):
    number = data[index]
    listA = []
    listB = []
    for x in range(index - preamble_length, index):
        listA.append(data[x])
        listB.append(data[x])

    for a in listA:
        for b in listB:
            if((a+b == number) and (a != b)):
                return False
    return True

for x in range(preamble_length, len(lines)):
    value = check(lines, x)
    if(value):
        number = lines[x]
        break

begin = 0
end = 0
while begin <= len(lines):
    data = lines[end:begin]
    if len(data) < 2:
        begin += 1
    current = sum(data)
    if (current == number):
        print(max(data) + min(data))
        break
    elif (current < number):
        begin = begin + 1
    elif (current > number):
        end = end + 1