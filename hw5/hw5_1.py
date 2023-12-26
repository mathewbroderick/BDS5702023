
#ARGUMENTS EXPECTED: "Liver", "Kidney", "Heart" or "Brain" 

#!/usr/bin/python3

import sys

INPUT_VAR = sys.argv[1]

goodOrgans = ["Liver","Kidney","Heart","Brain"] 


if INPUT_VAR in goodOrgans:
	print("Performing test on " + INPUT_VAR + ".") 
else:
	print("Invalid Tissue. Valid tissues are: Liver, Kidney, Heart, or Brain. Exiting.")
	exit() 
