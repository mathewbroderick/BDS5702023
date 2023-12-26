#!/usr/bin/python3

import sys


if len(sys.argv) !=4 :
	print("Three arguments required. Exiting.")
	exit()
else:
	if len(sys.argv) == 4:
		arguments = sys.argv[1:]
		for i in arguments:
			if i == "5" or i == "6" or i == "7":
				print(f"{i} accepted.")
			else:	
				print(f"{i} is an invalid argument, not accepted.") 
