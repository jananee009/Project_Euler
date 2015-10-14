# Greatest product in a 20*20 grid
# Problem Source: https://projecteuler.net/problem=11


import numpy
import time


# this method takes the grid as input, transposes columns to rows and returns a matrix. 
def getAllColumns(originalMatrix):
	colMatrix = []
	for i in range(0,len(originalMatrix)):
		# extract each column from the original matrix.
		eachCol = [row[i] for row in originalMatrix] 
		# add each col as a row to the colMatrix. 
		colMatrix.append(eachCol)	
	return 	colMatrix


# this method takes the original matrix and returns the highest product of 4 adjacent numbers along any diagonal in the grid.
def getMaxDiagonalProduct(originalMatrix):	
	max_prod = 0
	for i in range(16):
		for j in range(16):
			prod = originalMatrix[i][j]*originalMatrix[i+1][j+1]*originalMatrix[i+2][j+2]*originalMatrix[i+3][j+3]
			if prod > max_prod: max_prod = prod		
	for i in range(3,20):
		for j in range(16):		
			prod = originalMatrix[i][j]*originalMatrix[i-1][j+1]*originalMatrix[i-2][j+2]*originalMatrix[i-3][j+3]
			if prod > max_prod: max_prod = prod
	return 	max_prod	


# given a matrix and the length of numbers to multiply at a time, this method returns the highest product.
def computeProduct(Matrix,prodlen):
	listOfProducts = []
	beg = 0
	end = 0
	for i in range(0,len(Matrix)):
		for j in range(0,(len(Matrix[i])-(prodlen-1))):
			prod = 1
			beg = j
			end = j+prodlen
			for k in range(beg,end):
				prod = prod * Matrix[i][k]
			listOfProducts.append(prod)		
	return max(listOfProducts)


		
# this method reads the grid of numbers in to a matrix (a list of lists).
def readAllNumbers():
	matrix = [[0]*20 for i in range(20)]
	f = open('Grid.txt','rU')
	i = 0
	for line in f:	
		strList = line.split(" ")
		for j in range(0,len(strList)-1):
			matrix[i][j] = int(strList[j])
		i = i+1			
	f.close()
	return matrix
	

def main():
	start_time = time.time()
	productLength = 4
	grid = readAllNumbers() # read all the numbers in a grid in to a matrix.
	maxRowProduct = computeProduct(grid,productLength)
	columnMatrix = getAllColumns(grid)
	maxColProduct = computeProduct(columnMatrix,productLength)
	maxDiagProduct = getMaxDiagonalProduct(grid)
	print "The greatest product of four adjacent numbers in the same direction  in the 20*20 grid is: ", max(maxRowProduct,maxColProduct,maxDiagProduct)
	print "Solution found in" , (time.time()-start_time), "seconds."



if __name__ == "__main__":
	main()

# Answer: 70600674	