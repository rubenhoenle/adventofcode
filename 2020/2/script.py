#!/usr/bin/python3

def findBetween(s, start, end):
  return (s.split(start))[1].split(end)[0]

def countChar(c, s):
	count = 0
	for x in s: 
		if (x == c): 
			count = count + 1
	return count

def isLetter(index, c, s):
	if(s[index - 1] == c):
		return True
	return False

passwords = []
pos1 = []
pos2 = []
letter = []

# read the passwords from the file:
f = open('data.txt')
for line in f.readlines():
	passwords.append(findBetween(line, ': ', '\n'))
	pos2.append(int(findBetween(line, '-', ' ')))
	letter.append(findBetween(line, ' ', ':'))
	pos1.append(int(line.split('-')[0]))
f.close()

numberOfValids = 0

for i in range(len(passwords)):
	first = isLetter(pos1[i], letter[i], passwords[i])
	second = isLetter(pos2[i], letter[i], passwords[i])
	# hint: ^ is the exor operator in python
	if(first ^ second):
		numberOfValids = numberOfValids + 1

print(numberOfValids)
