#!/usr/bin/python3

import sys


rangesInput = sys.argv[1]

studyInput = sys.argv[2]

outputStr = sys.argv[3]

rabng = {} 

with open(rangesInput, 'r') as rangesInFile:
	for rangeLines in rangesInFile:
		rangeA = rangeLines.strip()
		rangeB = rangeA.replace('\t', ' ')
		rangeC = rangeB.split(' ')
		start = float(rangeC[0])
		fin = float(rangeC[1]) 
		omg = f"{start}_{fin}"
		rabng[omg] = {} 
		#this all works
		with open(studyInput, 'r') as studyInFile:
			header = studyInFile.readline()
			for studyLines in studyInFile:	
				studyA = studyLines.strip()
				studyB = studyLines.split('\t')
				if 'NA' not in studyB[1:]:
					genes = studyB[0]	
					liverGood = [float(studyB[3]), float(studyB[8]), float(studyB[13])]
		
					avgLiverGood = sum(liverGood) / len(liverGood)
					if start <= avgLiverGood <= fin:
						rabng[omg][genes] = []	
						rabng[omg][genes].append(avgLiverGood)  	

for i, j in rabng.items():
	okayfinalfile = f"{outputStr}_{i}_range.txt"
	with open(okayfinalfile, 'w') as outFile:
		for j, k in j.items():
			final = f"{j}\t{k}\n"
			outFile.write(final)   	 
