#!/usr/bin/python3

def isValid(passport):
	fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	for field in fields:
		if not (str(field + ':') in passport):
			return False
	return True

lines = []

f = open('data.txt')
for line in f.readlines():
	lines.append(str(line.split('\n')[0]))
f.close()

lines.append('')

passports = []
s = ''

for line in lines:
	if (line == ''):
		passports.append(s)
		s = ''
	else:
		s = s + line	

valid = 0

for passport in passports:
	#print(passport + str (isValid(passport)))
	if(isValid(passport)):
		valid = valid + 1


print('Number of valid passports: ' + str(valid))
