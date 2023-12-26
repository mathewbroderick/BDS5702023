#Arguments expected: "Liver", "Kidney", "Heart" or "Brain"

#!/usr/bin/python3

import sys

INPUT_VAR = sys.argv[1]

goodOrgans = ["Liver","Kidney","Heart","Brain"]

if INPUT_VAR not in goodOrgans:
	print("Invalid Tissue. Valid tissues are: Liver, Heart, Kidney, or Brain. Exiting.")
else:
	print("Performing test on " + INPUT_VAR + ".") 
