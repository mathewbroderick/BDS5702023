#!/usr/bin/bash
# iCluster: a program that takes an input file with any number of datapoints that have an x, y index seperated by tab and outputs a file containing a list of clusters with the points assigned to the nearest cluster center
#
#	general usage: ./cluster2d.py [NUMBER OF CLUSTERS DESIRED] [MAX NUMBER OF ITERATIONS] [INPUT TEXT FILE] [DESIRED NAME OF OUTPUT FILE]
#	example: ./cluster2d.py 7 100 datapoints.txt output.txt
#
#	usage notes:
#	> this is the "verbose" version of this program, that will print the iteration number and new cluster centers for each iteration
#	>run run_cluster2d_quiet.sh to not see command line output
#	>this program does accept input files with headers and will recognize and skip a header as long as the header does not start with a number or - (i feel like you would only do that if you wanted to hurt my feelings :( )
#	>you can specify a path for the input file
#	>general advice for naming output file is the format [currentdate]finalclusters.txt but you can name it whatever you want 

./cluster2d.py 7 100 set_2_datapoints.txt output.txt 
