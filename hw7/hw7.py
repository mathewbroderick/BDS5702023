#!/usr/bin/python3
#if youre reading this: this assignment was blood sweat and tears. im gonna go play russian fishing 4 for 67 hours straight. 
import sys


input = sys.argv[1] 

output = sys.argv[2] 


final_file = open(output, "w") 



with open(input, 'r') as inFile:
	die = inFile.readline()
	final_file.write(die) 

	for lines in inFile:

		A = lines.strip()
		B = A.split('\t')
		if B[1] == 'Y': 
			if 'NA' not in B[1:]:
				if float(B[6]) <= -1.5 and float(B[11]) <= -1.5 and float(B[16]) <= -1.5:
					if float(B[3]) > 2.0 or float(B[8]) > 2.0 or float(B[13]) > 2.0: 
						if float(B[3]) > 1.5 and float(B[8]) > 1.5 and float(B[13]) > 1.5:
							final_file.write('\t'.join(B) + '\n' )	










 
		 
