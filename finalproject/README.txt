

_________ _______  _                 _______ _________ _______  _______ 
\__   __/(  ____ \( \      |\     /|(  ____ \\__   __/(  ____ \(  ____ )
   ) (   | (    \/| (      | )   ( || (    \/   ) (   | (    \/| (    )|
   | |   | |      | |      | |   | || (_____    | |   | (__    | (____)|
   | |   | |      | |      | |   | |(_____  )   | |   |  __)   |     __)
   | |   | |      | |      | |   | |      ) |   | |   | (      | (\ (   
___) (___| (____/\| (____/\| (___) |/\____) |   | |   | (____/\| ) \ \__
\_______/(_______/(_______/(_______)\_______)   )_(   (_______/|/   \__/
                                                                        

---ACSII art from https://patorjk.com---
---program written by Alex K.---
---moral support provided by Allie ૮ ・ﻌ・ა---

Enjoy using iCluster!

Quick start: ./run_cluster2d.sh -v (verbose or not) -n [number of clusters desired, or k] -i [max number of iterations, program will automatically stop when converged] -f [input file] -o [desired name of output file]

Example: ./run_cluster2d.sh -v -n 8 -i 100 -f datapoints.txt -o output.txt

______________________________________________________

Parameters:
> -v: verbose/non-verbose. if -v is specified, command line output will be provided which lists the number of iterations and the cluster centers of each iteration. if this flag isn't used, the program will only print if the header is detected or not, and if/when the program is converged

> -n number of final clusters/cluster centers desired, should be a whole number (why wouldnt it be?)

> -i max number of iterations desired, this is the number of times that the centers are regenerated. the program will stop anyways when the centers are identical from one iteration to the next. 

> -f input file, should be a text file (not csv) of lines with two numerical values (x and y coordinates) separated by a tab. The file can have a header as long as it doesn't start with a number or minus sign. The values can be negative. There should be no additional spaces or characters between the values. An example of this format can be seen below. 
0.66    0.66
0.5     0.42
0.36    0.74
0.65    0.81
0.33    0.47
0.71    0.66
0.51    0.79
0.34    0.43

> -o the desired name of the output file, should be a .txt file. The program also outputs a file called clusters.txt, which contains the final cluster centers, generally used for visualization 

If the user really, really wants to edit a shell script they can run the programs through run2dcluster_verbose.sh or run2dcluster_quiet.sh. The user input needed is specified in the respective shell script.

_____________________________________________________

OTHER FUNCTIONALITY:

plot_clusters.sh is a shell script that calls plot_clusters2.py which in turn creates a image called "cluster_plot.png" which is a visual graph of the clusters with their respective centers. The program required that the output file is called output.txt and the centers file is centers.txt.

test_output.sh is a bash script that compares the points in the input file to the points in the output file, to make sure they're the same. This doesn't really like whole numbers so will flag those as missing. 

there are three sets of datapoints available in the folder for testing the program-one with a header. Feel free to experiment with these.
