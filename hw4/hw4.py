#!/usr/bin/python3

import sys


seq = ["G","C","A","T"]

seqTwo = seq.copy() 

fourMers = []

posOne = sys.argv[1] 

posTwo = sys.argv[2] 

#counters? whyd it have to be counters?????

indexCounter = 0

indexCounterTwo = 0


while indexCounter < len(seq):
	i = seq[indexCounter]
	while indexCounterTwo < len(seqTwo):
		j = seqTwo[indexCounterTwo]
		fourMers.append(posOne + i + posTwo + j) 
		indexCounterTwo += 1
	indexCounterTwo = 0
	indexCounter += 1

for k in fourMers: 
	print(k)  


print("The total number of possibilities is:")

print(len(fourMers))
