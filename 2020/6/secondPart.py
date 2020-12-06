#!/usr/bin/python3

import string

ugly_lines = []

f = open('data.txt')
for line in f.readlines():
	ugly_lines.append(str(line.split('\n')[0]))
f.close()

ugly_lines.append('')

groups = []

s = ''

for line in ugly_lines:
	if(line == ''):
		s = s[:-1]
		groups.append(s)
		s = ''
	else:
		s = s + line + ' '

print(groups)

chars = list(string.ascii_lowercase)

count = 0

for group in groups:
	#answers = []
	answers = group.split()
	print(answers)
	for c in chars:
		found = False
		for answer in answers:
			if (c in answer):
				found = True
			else:
				found = False
				break
		if (found):
			count += 1
		
	

print('Number of questions answered with yes: ' + str(count))