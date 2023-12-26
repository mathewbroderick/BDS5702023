#!/usr/bin/python3

import sys

posOne = sys.argv[1]

posThree = sys.argv[2]

nList = ["G", "C", "A", "T"]



for i in range(0, len(nList)):
	tresMers = nList[i]
	print(f"{posOne}{tresMers}{posThree}")





print("The total number of possibilities is:")

print(len(nList)) 
