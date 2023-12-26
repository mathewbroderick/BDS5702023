#!/usr/bin/python3

import sys

goodnumbers = ["5","6","7"]
if len(sys.argv) !=4 :
	print("Three arguments required. Exiting.")
	exit()
else:
	if len(sys.argv) == 4:
		arguments = sys.argv[1:]	
		for i in arguments:
			if i in goodnumbers:  
				print(f"{i} accepted.")
			else:
				print(f"{i} is an invalid argument, not accepted.")


