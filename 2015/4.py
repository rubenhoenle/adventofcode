#!/usr/bin/python3

import hashlib
from aoctools import InputReader, Part

input = "yzbqklnj"

def calc(key: str, zeroes: int):
	i = 0
	while True:
		result = hashlib.md5((input + str(i)).encode()).hexdigest()
		if str(result).startswith("0" * zeroes):
			return i
		i += 1

print("Part 1:", calc(input, 5)) #282749
print("Part 2:", calc(input, 6)) #9962624
