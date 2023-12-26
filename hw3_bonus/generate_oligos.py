#!/usr/bin/python3

import sys

args = sys.argv

k = int(args[1]) 
 
seq = ["G","C","A","T"] 

kmers = [""] 


for i in range(k):
	kmers = [j + l for j in kmers for l in seq]

for j in kmers:
	print(j)

print(len(kmers)) 
