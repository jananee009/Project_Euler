# Problem 18: Maximum path sum I
# problem Source: https://projecteuler.net/problem=18


import math
import time


# reads each row of the triangle in to a list. Stores the entire triangle as a list of lists.
def readTriangle(): 
	list_of_lists = []
	triangle = open("Problem18-Data.txt","r")
	lines = triangle.read().split('\n')
	for line in lines:
		line1 = []
		line1 = line.split(' ')
		list_of_lists.append(line1)
	for i in range(0,len(list_of_lists)):
		for j in range(0,len(list_of_lists[i])):
			list_of_lists[i][j] = int(list_of_lists[i][j])	
	return	list_of_lists	



def findMaxPath():
	triangle = readTriangle()
	for i in range(13,-1,-1): # start from the 2nd last row of the triangle and work your way up. i corresponds to each row of the triangle.
		for j in range(len(triangle[i])): # j corresponds to each element in a row.
			triangle[i][j] += max(triangle[i + 1][j],triangle[i + 1][j + 1])
	return triangle[0]			


def main():
	start_time = time.time()
	print "Calling function........"
	print "Maximum Path Sum is: ",findMaxPath()
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	

# Answer: 1074	