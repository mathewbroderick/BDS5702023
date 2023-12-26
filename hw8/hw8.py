#!/usr/bin/python3


import sys


inputTable = sys.argv[1] 
inputStudy = sys.argv[2] 
output = sys.argv[3] 

indexDic = {}

with open(inputTable, 'r') as inFile:
	for lines in inFile:

		A = lines.strip()
		B = A.split('\t')
		for i in B:
			if B[1] == "NA":
				print(f"Alert, NA value encountered in homogenate value for {B[0]}")
				pass
			else: 
				indexDic[B[0]] = float(B[1])



with open(inputStudy, 'r') as studyInFile, open(output, 'w') as outFile:
	header = studyInFile.readline()
	outFile.write("Gene\tHomog\tKidney\n")	
	for studyLines in studyInFile:
		studyA = studyLines.strip()
		studyB = studyA.split('\t') 
		genes = studyB[0]
		if genes not in indexDic:
			print(f"Alert, the homogenate value for {genes} could not be identified in the file {inputTable}")
			pass
		else:	
			kidneyTime = [float(studyB[6]) if studyB[6] != 'NA' else 'NA', float(studyB[11]) if studyB[11] != 'NA' else 'NA', float(studyB[16]) if studyB[16] != 'NA' else 'NA']
			if 'NA' in kidneyTime:
				print(f"Alert, NA value encountered in Kidney replicates for {genes}")
				pass
			else:	
				homo = indexDic[genes]

				finalKidney = sum(kidneyTime)/len(kidneyTime)

				if finalKidney > homo:
					outFile.write(f"{genes}\t{homo}\t{finalKidney}\n")	
				 



 
		 
