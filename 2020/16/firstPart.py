#!/usr/bin/python3

lines = []
f = open('data.txt')
for line in f.readlines():
    lines.append(line.split('\n')[0])
f.close()

possibles = []
for line in lines:
    if(line == ''):
        break
    words = line.split()
    for word in words[:]:
        if not ('-' in word):
            words.remove(word)
    
    for word in words:
        temp = word.split('-')
        for t in range(int(temp[0]), int(temp[1]) + 1):
            if (int(t) not in possibles):
                possibles.append(t)

value = 0
u = lines.index('nearby tickets:')
for i in range(u + 1, len(lines)):
    numbers = lines[i].split(',')
    for number in numbers:
        if (int(number) not in possibles):
            value += int(number)
    
print(value)
