#!/usr/bin/bash
#NOT FOR USER EDITING- did you read the README.txt before sniffing around?
#this bash script is called when the user wants to call the program from the command line
#example usage (which you should know from the readme): ./run_cluster2d.py -v (specific this flag for verbose or not) -n NUMBER OF CLUSTERS -i MAX ITERATIONS -f INPUT FILE NAME -o DESIRED OUTPUT FILE NAME 


verbose=false
k=""
maxiterations=""
input=""
output="" 

while [ "$#" -gt 0 ]; do
	case $1 in
		-v)	
			verbose=true
			;;
		-n)
			k="$2"
			shift
			;;
		-i)
			maxiterations="$2"
			shift
			;;
		-f)
			input="$2"
			shift
			;;
		-o)
			output="$2"
			shift
			;;
		*)	

			echo "Unknown flag: $1"
			exit 1
			;;
	esac
	shift
done

if [ -z "$k" ] || [ -z "$maxiterations" ] || [ -z "$input" ] || [ -z "$output" ]; then
	echo "Unknown flags. Usage: $0 -v (verbose or not) -n NUMBER OF CLUSTERS -i MAX ITERATIONS -f INPUT FILE -o OUTPUT FILE"
	exit 1
fi
 
if [ "$verbose" = true ]; then
	python cluster2d.py "$k" "$maxiterations" "$input" "$output" 
else
	python cluster2dquiet.py "$k" "$maxiterations" "$input" "$output"	
fi

