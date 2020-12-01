#!/usr/bin/python3

numbers = []

# read the numbers from the file:
f = open('data.txt')
for line in f.readlines():
    numbers.append(int(line))
f.close()

for a in numbers:
	for b in numbers:
		if((a + b) == 2020):
			print(str(a) + " + " + str(b) + " = " + str(a+b))
			print(str(a) + "*" + str(b) + " =  " + str(a*b))
