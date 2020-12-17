#!/usr/bin/python3

# returns the first/second/third/... values of all nearby tickets
def getValues(index, lines):
    u = lines.index('nearby tickets:')
    values = []
    for i in range(u + 1, len(lines)):
        numbers = lines[i].split(',')
        values.append(int(numbers[index]))
    return values

# returns the number of values each ticket has
def getNumberOfValues(lines):
    u = lines.index('nearby tickets:') + 1
    numbers = lines[u].split(',')
    return len(numbers)

# returns the possible values in a list of a single rule
def getPossibles(line):
    words = line.split()
    for word in words[:]:
        if not ('-' in word):
            words.remove(word)
    ps = []
    for word in words:
        temp = word.split('-')
        for t in range(int(temp[0]), int(temp[1]) + 1):
            if (int(t) not in ps):
                ps.append(t)
    return ps

# checks if all values are in the possibles list
def check(values, possibles):
    for v in values:
        if (v not in possibles):
            return False
    return True

# removes all invalid tickets from the list
def removeInvalidTickets():
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

    invalid = []
    u = lines.index('nearby tickets:')
    for i in range(u + 1, len(lines)):
        numbers = lines[i].split(',')
        for number in numbers:
            if (int(number) not in possibles):
                invalid.append(i)

    for index in sorted(invalid, reverse=True):
        del lines[index]

    return lines

# removes the given value from a nested list
def remove(values, remove_value):
    for vl in values[:]:
        try:
            vl.remove(remove_value)
        except ValueError:
            pass
    return values

############################################
#                                          #
#    START OF PROGRAMM                     #
#                                          #
############################################

# read the data from the file
lines = []
f = open('data.txt')
for line in f.readlines():
    lines.append(line.split('\n')[0])
f.close()

# remove the invalid tickets
lines = removeInvalidTickets()

# get all possibles
possibles = []
for x in range(len(lines)):
    if(lines[x] == ''):
        break
    possibles.append(getPossibles(lines[x]))

# get the values row by row from the nearby tickets
values = []
for v in range(getNumberOfValues(lines)):
    values.append(getValues(v, lines))

# get all possible rules for each row
solution = []
temp = []
for vs in values:
    ts = []
    for ps in possibles:
        if (check(vs, ps)):
            ts.append(lines[possibles.index(ps)])
    if ts:
        temp.append(ts)

# search the right rule for each row 
done = []
do = True
while do:
    for tp in temp:
        if(len(tp) == 1):
            s = tp[0]
            if(s not in done):
                temp = remove(temp, s)
                tp.append(s)
                done.append(s)
                break
    do = False 
    for tp in temp:
        if(len(tp) > 1):
            do = True

solution = temp[:]
rows = []

# get the rows indexes according to the department rules
for sl in solution:
    s = sl[0]
    if('departure' in s):
        rows.append(solution.index(sl))

# get the index of my ticket
u = lines.index('your ticket:') + 1

words = lines[u].split(',')
values = []
for word in words:
    if(words.index(word) in rows):
        values.append(int(word))

# multiply the values
solution = 1
for value in values: 
    solution = solution * value
print(solution)
