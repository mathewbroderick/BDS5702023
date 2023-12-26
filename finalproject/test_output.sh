#!/usr/bin/bash
#replace input and output files in this script as needed
awk 'FNR==NR {seen[$1,$2]++; next} {print $1, $2, (seen[$1,$2] ? "present" : "missing")}' set_1_datapoints.txt output.txt | grep "missing" 
