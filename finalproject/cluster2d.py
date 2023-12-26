#!/usr/bin/python3

#importing needed modules, random module functionality is drawing random values between two given values   
import random
import sys

#processing user input: first argument is the input for k, the number of clusters desired 
#second argument is max number of iterations (of re-assigning the cluster centers) allowed, so the program will stop	
#generating new centers even if convergance (new cluster centers = old cluster centers) hasn't been reached
#third argument is the name of the input file, txt file expected (not csv)
#fourth argument is the name of the output file, which should have all the same points as the input file, just
#reassigned to clusters 

kInput = int(sys.argv[1])
maxIterations = int(sys.argv[2])
inputFile = sys.argv[3]
outputfileName = sys.argv[4]

#defining the function for Euclidean distance 
def eDist(x,y,p,q):
	return ((x-p)**2+(y-q)**2)**0.5 
#creating the empty list to store data points in, the loop below seperates the data points by x and y values, converts
#them to floating point numbers, then adds them as a set to the coords list 
#some added functionality: reading the first object of the file and finding out if the file is a header or not
#only problem: if the header's first element is a minus sign this doesn't /really/ work and would probably break the program 

coords = []
with open(inputFile, 'r') as inFile:
	first = next(inFile)
	if not first[0] == '-':
		if type(first[0]) == int or type(first[0]) == float:
			print('No header detected, proceeding.')	
		else:
			print('Header detected, skipping.')		
			head = inFile.readline() 
	else:
		print('No header detected, proceeding.') 
	for lines in inFile:
		A = lines.strip()
		B = A.split('\t')
		x = float(B[0])
		y = float(B[1])
		coords.append((x, y))

#setting the original cluster centers: the min and max functions work on one side of each tuple respectively
#and the "for i in range(kInput)" line allows the center to be set k amount of times
#the final product is simple: a list of k number of coordinates drawn randomly from the x and y ranges 

clusterCenters = [(random.uniform(min(x for x, y in coords), max(x for x, y in coords)), random.uniform(min(y for x, y in coords), max(y for x, y in coords))) for i in range(kInput)]

#this is the for loop that reassigns the cluster centers

for iter in range(maxIterations): #this sets the loop to only run the number of times that the user gave it for the max iteration 
	print(f"Iteration {iter + 1}") #line that prints the iteration the loop is on 
	clusters = {i + 1: [] for i in range(kInput)} #this sets up the dictionary about to be used for storing cluster values, the keys being kInput + 1 (since the python indexing starts at 0) and the pair value being an empty list 
	for x, y in coords:
		distances = [eDist(x, y, cx, cy) for cx, cy in clusterCenters] #calling the eDist function for each index in each element of the cluster_centers list, and adding the output to a list 
		clostestCluster = distances.index(min(distances)) + 1 #using the index function to find the minimum value in the new distances list, and setting the clostest cluster to this index 
		clusters[clostestCluster].append((x, y)) #adding the coords to the clostest cluster value seen above
	newCenters = [] #setting up the empty dictionary for the new centers 
	for cluster in clusters.values(): #running a loop for each cluster value (which is currently set up like {CLUSTER NUMBER : [LIST OF COORDS]} so the values are just the lists) 
		if cluster: #making sure that there are actually elements in the list: this WILL break the code if not implemented 
			xsum = sum(x for x, y in cluster) #taking the sum of the x values in the cluster
			ysum = sum(y for x, y in cluster) #taking the sum of the y values in the cluster	

			centerx = xsum / len(cluster) #finding the average of the sum of the x values 
			centery = ysum / len(cluster) #rinse and repeat 
			newCenters.append((centerx, centery)) #adding both to the new centers list
		else:
			newCenters.append(clusterCenters[-1]) #if not: adding the old cluster centers to the new centers list 

	if clusterCenters == newCenters: #if the old centers (pre-loop) are equal to the new centers (post loop, stored in a list) print converged and break the entire loop 
		print("Converged!")
		break
	clusterCenters = newCenters #otherwise, reassign the newCenters (found in the list at the top of the code) to the clusterCenters 

	print("New Cluster Centers:")
	for center in clusterCenters:
		print(center)


with open('centers.txt', 'w') as outFile:
	for center in clusterCenters:
		x, y = center	
		outFile.write(f"{x}\t{y}\n") 


with open(outputfileName, 'w') as outFile:
	outFile.write("X\tY\tCluster\n")
	for cluster_num, points in clusters.items():
		for x, y in points:
			outFile.write(f"{x}\t{y}\t{cluster_num}\n") 









#code graveyard :(
'''
xValue = []
yValue = []
needthis = []
with open(inputFile, 'r') as inFile:
	header = inFile.readline()
	for lines in inFile:
		A = lines.strip()
		B = A.split('\t')
		needthis.append(B)	
		xValue.append(float(B[0])) 
		yValue.append(float(B[1])) 
lowxvalue = min(xValue)
highxvalue = max(xValue)
highyvalue = max(yValue)
lowyvalue = min(yValue)
cnt = 0	
bigDic = {}
while cnt < kInput: 
	draw_floaty = random.uniform(lowyvalue, highyvalue)	
	draw_floatx = random.uniform(lowxvalue, highxvalue) 
	k = cnt+1	
	testlist = []
	for i in needthis: 
		xval = float(i[0])
		yval = float(i[1])
		p = eDist(xval,yval,draw_floatx,draw_floaty)
		testlist.append({f"{xval} {yval}": p})
		
	bigDic[k] = testlist		
	cnt +=1 
final = {}
for iter in range(maxIterations): 
	print(f"Iteration {iter + 1}")
	for i, j in final.items():
		print(f"Cluster {i}: {len(j)} points") 

	bigdicTwo = {}
	for i, j in bigDic.items():
		for k in j:
			for m, n in k.items():
				if m not in bigdicTwo or n < bigdicTwo[m]['Enumber']: 
					bigdicTwo[m] = {'clusternumber': i, 'Enumber': n} 

	final = {}	
	for i, j in bigdicTwo.items():
		clusternum = j['clusternumber']
		if clusternum not in final:
			final[clusternum] = []
		final[clusternum].append(i)
	for i,j in final.items():
		coordinateslist = final[i]	
		xavg = 0
		yavg = 0
		for k in coordinateslist:
			x, y =map(float, k.split())
			xavg += x
			yavg += y
		newcenterx = xavg / len(coordinateslist)
		newcentery = yavg / len(coordinateslist)
		print(f"Coordinates assigned to Cluster {i}: {coordinateslist}")	
		print(f"Cluster {i} center: {newcenterx}, {newcentery}")	
		bigDic[i] = [{" ".join([str(newcenterx), str(newcentery)]) : 0}]	
	converged = True	
	for i, j in bigDic.items():
		newcenter = list(j[0].keys())[0].split()
		newcenterx, newcentery = float(newcenter[0]), float(newcenter[1])
 
		oldcenter = list(j[0].keys())[0].split()
		oldcenterx, oldcentery = float(oldcenter[0]), float(oldcenter[1])
		if abs(newcenterx - oldcenterx) >= 0.001 or abs(newcentery - oldcentery) >= 0.001:
			converged = False
			break
	if converged:
		break  	
with open(outputfileName, 'w') as outFile:
	outFile.write("X\tY\tCluster\n")
	for clusternum, j in final.items():
		for k in j:
			x, y =  map(float, k.split()) 
			outFile.write(f"{x}\t{y}\t{clusternum}\n")

'''
