#!/usr/bin/python3

f = open('input.txt', 'r')

lines = f.readlines()

numbers = []
for line in lines:
	numbers.append(int(line))

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


i = 0
sums = []
twiceVal = -99

while True:
	for number in numbers:
		i = i + number
		#print(number)
		#print(i)
		#print(sums)
		#print("--------------------")
		if(i in sums):
			print(i)
			quit()	
		sums.append(i)

	#print(sums)
	#print(twiceVal)
	#print(i)

	#for s in sums:
	#	if(countX(sums, s) > 1):
	#		print("+ + + SOLUTION FOUND:  + + +")
	#		print(s)
	#		quit()
