#!/usr/bin/python3

import sys

posOne = sys.argv[1]

posTwo = sys.argv[2]

nList = ["G", "C", "A", "T"]    

nListDos = ["G", "C", "A", "T"]
 
for i in nList: 
	for j in nListDos: 
		print(f"{posOne}{i}{posTwo}{j}") 





print("The total number of possibilities is:")
print(len(nList)*2 + len(nListDos)*2)
