#!/usr/bin/python3

def isValid(passport):
	fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	for field in fields:
		if not (str(field + ':') in passport):
			return False
	return True

def findBetween(s, start, end):
  return (s.split(start))[1].split(end)[0]

def checkDetails(passport):
	attributes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	
	values = []
	for attribute in attributes:
		values.append(findBetween(passport, attribute + ':', ' '))

	birthyear = checkBirthYear(values[0])
	issueyear = checkIssueYear(values[1])
	expirationyear = checkExpirationYear(values[2])
	height = checkHeight(values[3])
	haircolor = checkHairColor(values[4])	
	eyecolor = checkEyeColor(values[5])
	passportid = checkPassportID(values[6])

	if(eyecolor and birthyear and issueyear and expirationyear and height and haircolor and passportid):
		return True
	return False

def checkPassportID(s):
	if ((len(s) == 9) and s.isdigit()):
		return True
	return False

def checkBirthYear(s):
	year = int(s)
	if((year >= 1920) and (year <= 2002)):
		return True
	return False

def checkIssueYear(s):
	year = int(s)
	if((year >= 2010) and (year <= 2020)):
		return True
	return False

def checkExpirationYear(s):
	year = int(s)
	if((year >= 2020) and (year <= 2030)):
		return True
	return False

def checkHeight(s):
	end = s[-2:]
	#cm
	if(end == 'cm'):
		s = s.replace('cm', '')
		size = int(s)
		if((size >= 150) and (size <= 193)):
			return True
	#in
	if(end == 'in'):
		s = s.replace('in', '')
		size = int(s)
		if((size >= 59) and (size <= 76)):
			return True
	return False

def checkEyeColor(s):
	colors = ['amb', 'blu',  'brn', 'gry', 'grn', 'hzl', 'oth']
	for color in colors:
		if(s == color):
			return True
	return False

def checkHairColor(s):
	if not (s[0] == '#'):
		return False
	s = s.replace('#', '')
	if not (len(s) == 6):
		return False
	chars = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for x in range(len(s)):
		if not (s[x] in chars):
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
		s = s + ' '
		passports.append(s)
		s = ''
	else:
		s = s + ' ' + line	

valid = 0
pps = []

for passport in passports:
	if(isValid(passport)):
		if(checkDetails(passport)):
			valid = valid + 1


print('Number of valid passports: ' + str(valid))