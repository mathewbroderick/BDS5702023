#!/usr/bin/python3


import sys


high = float(sys.argv[1])
low = float(sys.argv[1])



for i in range(2, len(sys.argv)):
	number = float(sys.argv[i])

	if number > high:
		high = number
	if number < low:
		low = number


print("min =", low)
print("max =", high) 
