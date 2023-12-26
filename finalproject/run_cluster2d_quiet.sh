#!/usr/bin/bash
# iCluster: a program that takes an input file with any number of datapoints that have an x, y index seperated by tab and outputs a list of clusters with the points assigned to the nearest cluster
#
#	general usage: ./cluster2dquiet.py [NUMBER OF CLUSTERS DESIRED] [MAX NUMBER OF ITERATIONS] [INPUT TEXT FILE] [DESIRED NAME OF OUTPUT FILE]
#	example: ./cluster2d.py 7 100 datapoints.txt output.txt
#
#	usage notes:
#	> this is the "quiet" version of this program, that does not print the iteration number and new cluster centers for each iteration
#	>run run_cluster2d_verbose.sh to see command line output
#	>this program does accept input files with headers and will recognize and skip a header as long as the header does not start with a number or - (i feel like you would only do that if you wanted to hurt my feelings :( )
#	>general advice for naming output is the format [currentdate]finalclusters.txt but you can name it whatever you want 

./cluster2dquiet.py 7 100 set_1_datapoints.txt output.txt 
