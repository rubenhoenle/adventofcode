#!/usr/bin/python3

import string

class Bagrule:
	def __init__(self, bagcolor):
		self.rules = []
		self.bagcolor = bagcolor
		self.contain = False

	def getBagcolor(self):
		return self.bagcolor

	def addRule(self, rule):
		self.rules.append(rule)

	def getRules(self):
		return self.rules

	def canContain(self):
		self.contain = True

	def getContain(self):
		return self.contain

def calc(s, bags):
	for bag in bags:
		if (s in bag.getRules()):
			bag.canContain()
			calc(bag.getBagcolor(), bags)

ugly_lines = []

f = open('data.txt')
for line in f.readlines():
	ugly_lines.append(str(line.split('\n')[0]))
f.close()

bags = []

for line in ugly_lines:
	# split the line into the single words
	words = line.split()
	bagrule = Bagrule(words[0] + ' ' + words[1])

	if not('contain no other bags' in line):
		# remove the first 4 words from the list
		for i in range(4):
			words.remove(words[0])

		# remove all words containing 'bag' or only digits from the list
		for word in words[:]:
			if(('bag' in word) or (word.isdigit())):
				words.remove(word)

		# add the rules to the bagrule object
		x = 0	
		while (x in range(len(words) - 1)):
			bagrule.addRule(words[x] + ' ' + words[x + 1])
			x += 2

	bags.append(bagrule)

count = 0

calc('shiny gold', bags)

for bag in bags:
	if(bag.getContain()):
		count += 1

print('Number of shiny gold bags: ' + str(count))