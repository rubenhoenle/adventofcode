#!/usr/bin/python3

def findBetween(s, start, end):
  return (s.split(start))[1].split(end)[0]

def countChar(c, s):
	count = 0
	for x in s: 
		if (x == c): 
			count = count + 1
	return count

passwords = []
minimal = []
maximal = []
letter = []

# read the passwords from the file:
f = open('data.txt')
for line in f.readlines():
	passwords.append(findBetween(line, ': ', '\n'))
	maximal.append(int(findBetween(line, '-', ' ')))
	letter.append(findBetween(line, ' ', ':'))
	minimal.append(int(line.split('-')[0]))
f.close()

numberOfValids = 0

for i in range(len(passwords)):
	numberOfLetter = countChar(letter[i], passwords[i])
	if((numberOfLetter >= minimal[i]) and (numberOfLetter <= maximal[i])):
		numberOfValids = numberOfValids + 1

print(numberOfValids)
