#!/usr/bin/python3

lines = []
used = []

f = open('data.txt')
for line in f.readlines():
    lines.append(int(line))
    used.append(False)
f.close()

one = 0
three = 0

current = 0

ratings = [1, 2, 3]
while (False in used):
    for r in ratings:
        if((current + r) in lines):
            index = lines.index(current + r)
            if not (used[index]):
                if(r == 1):
                    one += 1
                elif (r == 3):
                    three += 1
                current = lines[index]
                used[index] = True
                stop = True
                break

three += 1

print(one * three)