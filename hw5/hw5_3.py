#!/usr/bin/python3


import sys

bummber = float(sys.argv[1])
 

if 1.2 <= bummber <= 6.7:
	print("Argument in valid range, accepted.")
elif 20.5 <= bummber <= 30.6:
	print("Argument in valid range, accepted.")
else:
	print("Invalid entry.")


