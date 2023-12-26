#!/usr/bin/python3

import sys


rangesInput = sys.argv[1]

studyInput = sys.argv[2]

outputStr = sys.argv[3]


with open(rangesInput, 'r') as rangesInFile:
	for rangeLines in rangesInFile:
		rangeA = rangeLines.strip()
		rangeB = rangeA.replace('\t', ' ')
		rangeC = rangeB.split(' ') 
		start = float(rangeC[0])
		fin = float(rangeC[1])
		
		okayfinalfile = f"{outputStr}_{start}_{fin}_range.txt"
		with open(studyInput, 'r') as studyInFile:
			header = studyInFile.readline()
			
			final = []

			for studyLines in studyInFile:	

				studyA = studyLines.strip()
				studyB = studyLines.split('\t')
				if 'NA' not in studyB[1:]:
					liverGood = [float(studyB[3]), float(studyB[8]), float(studyB[13])]
					avgLiverGood = sum(liverGood) / len(liverGood)
					if start <= avgLiverGood <= fin:
						final.append(studyLines)

			if final:
				with open(okayfinalfile, 'a') as yes:
					yes.writelines(final)











