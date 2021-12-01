#!/usr/bin/python3

numbers = []

# read the numbers from the file:
f = open('data.txt')
for line in f.readlines():
    numbers.append(int(line))
f.close()

for a in numbers:
	for b in numbers:
		for c in numbers:
			if((a + b + c) == 2020):
				print(str(a) + " + " + str(b) + " + "  + str(c)  + " = " + str(a+b+c))
				print(str(a) + "*" + str(b) + "*" + str(c) +  " =  " + str(a*b*c))
