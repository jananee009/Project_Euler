# Problem 18: Maximum path sum I
# Approach:
# Read all the numbers in the triangle in to lists. i.e.each row of the triangle will be read in to a separate list. 
# 


import math
import time



def readTriangle(): # read each row of the input triangle. Store each row in to a seperate list. All the rows (lists) will be stored in one another list. (i.e. list of lists).
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


def traverseTopToBottom():
	print "Traversing Top To Bottom ###############################################"
	fullTriangle = readTriangle()
	maxPathSum = 0
	maxIndex = 0 # list index of the highest value in a row
	maxValue = 0 #highest value in a row
	for i in range(0,len(fullTriangle)):
		if (i == 0):
			maxIndex = i
			maxValue = max(fullTriangle[i])
			maxPathSum = maxPathSum + maxValue
			print "Line: ",i
			print "Value: ",maxValue
			print "Index: ",maxIndex
		else:
			tempdict = {} # create a dictionary with key as adjacent indices and values as adjacent values to the current maximum value in a row
			tempdict = {maxIndex : fullTriangle[i][maxIndex] , maxIndex+1 : fullTriangle[i][maxIndex+1] }
			v = list(tempdict.values()) # get all values from the dictionary
			k = list(tempdict.keys()) #get all keys from the dictionary
			maxValue = max(v) # Get the max value from the dictionary
			maxIndex = k[v.index(maxValue)]
			maxPathSum = maxValue + maxPathSum
			print "******************************************"
			print "Line: ",i
			print "Value: ",maxValue
			print "Index: ",maxIndex
	print maxPathSum	
	return maxPathSum



def traverseBottomToTop(): # traverses the triangle from the last row to first row and returns the maximum path sum
		print "Traversing Bottom To Top##############################################"
		fullTriangle = readTriangle()
		
		maxIndex = 0
		maxValue = 0
		startIndex = len(fullTriangle)-1 # get the length of the last row of the triangle
		highestVal = max(fullTriangle[startIndex]) # Get the highest value of the last row
		highestIndex = [j for j, val in enumerate(fullTriangle[startIndex]) if val==highestVal] #get all the occurrences of the highest element in the list.
		maxPathSums = []
		for k in range(0,len(highestIndex)): # for each occurrence of the highest value in the last row, compute the maximum path sum. 
			print "starting from last row, index: ",highestIndex[k]
			maxPathSum = 0
			for i in range(len(fullTriangle)-1,-1,-1):
				if (i == len(fullTriangle)-1):
					maxIndex = highestIndex[k]
					maxValue = highestVal
					maxPathSum = maxPathSum + maxValue
					print "Line: ",i
					print "Value: ",maxValue
					print "Index: ",maxIndex
				else:
					tempdict = {} # create a dictionary with key as adjacent indices and values as adjacent values to the current maximum value in a row
					if (maxIndex > 0 and (maxIndex < len(fullTriangle[i])) ):
						tempdict = {maxIndex-1 : fullTriangle[i][maxIndex-1] , maxIndex : fullTriangle[i][maxIndex] }
						v = list(tempdict.values()) # get all values from the dictionary
						k = list(tempdict.keys()) #get all keys from the dictionary
						maxValue = max(v) # Get the max value from the dictionary
						maxIndex = k[v.index(maxValue)]
						maxPathSum = maxValue + maxPathSum
					elif(maxIndex == 0): # if maxIndex is equal to 0
						maxValue = fullTriangle[i][maxIndex]
						maxPathSum = maxValue + maxPathSum
					elif(maxIndex >= len(fullTriangle[i])):
						maxIndex = maxIndex-1
						maxValue = 	fullTriangle[i][maxIndex]
						maxPathSum = maxValue + maxPathSum
							
					print "******************************************"
					print "Line: ",i
					print "Value: ",maxValue
					print "Index: ",maxIndex
			maxPathSums.append(maxPathSum)		

		print maxPathSums	
		return max(maxPathSums)				
		 



def findMaxPath():
	maximumPathSums = []
	#maximumPathSums.append(traverseTopToBottom())
	maximumPathSums.append(traverseBottomToTop())
	print maximumPathSums
	return max(maximumPathSums)		





def main():
	start_time = time.time()
	print "Calling function........"
	print "Maximum Path Sum is: ",findMaxPath()
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	