# Greatest product in a 20*20 grid
# Approach: 1. First read the grid of numbers in to a matrix (i.e. a list of lists).
# 2. Each row in the grid corresponds to a list in the matix. It is also every easy to extract every column (in list form) from a matrix. 
# 3. For each list (row, column and diagonal), do the following:
# Starting from the first  number, compute the product of first 4 numbers. Store the product in a list.  
# Then starting from the second number,take the next 4 numbers and compute the product and store it in a list. Repeat the process until you reach the end of the row.
# Repeat this for all rows. 
# 4. Get the highest numebr from the product list which is the answer.  



import numpy



# this method takes the grid, transposes columns to rows and returns a matrix. 
def getAllColumns(originalMatrix):
	colMatrix = []
	for i in range(0,len(originalMatrix)):
		# extract each column from the original matrix.
		eachCol = [row[i] for row in originalMatrix] 
		# add each col as a row to the colMatrix. 
		colMatrix.append(eachCol)
	return 	colMatrix

# this method extracts all diagonal elements in the grid in to a list and returns a list of lists (i.e. a matrix).
def getAllDiagonals(originalMatrix):
	
	print originalMatrix
	print "length of original matrix: ",len(originalMatrix) 
	m = 0
	n = 0
	
	diagMatrix = []
	for i in range(0, len(originalMatrix)):
		for j in range(0,len(originalMatrix)):
			m = i
			n = j
			diaglist = []
			#diaglist.append(1000000)
			while(m != len(originalMatrix) and n != len(originalMatrix)): 
				print "Inside while loop"
				print "m: ", m
				print "n: ", n
				print "Element: ", originalMatrix[m][n]
				diaglist.append(originalMatrix[m][n])
				print "diaglist: ", diaglist 
				m = m+1
				n = n+1
			print "diaglist: ", diaglist 	
			diagMatrix.append(diaglist)	
	print diagMatrix	
	# remove those lists from the matrix that have fewer than 4 elements.

	for row in diagMatrix:
		if (len(row) < 4):
			diagMatrix.remove(row)
	return 	diagMatrix	


def computeProduct(Matrix,prodlen):
	listOfProducts = []
	beg = 0
	end = 0
	# row wise product
	print Matrix
	#print "row wise product" 	
	for i in range(0,len(Matrix)):
		print "processing row:",i
		for j in range(0,(len(Matrix[i])-(prodlen-1))):
			prod = 1
			beg = j
			end = j+prodlen
			#print "beg is:", beg
			#print "end is:", end
			for k in range(beg,end):
				print "Row: ",i
				print "Column: ",k
				print "number: ",Matrix[i][k]
				prod = prod * Matrix[i][k]
				print "prod: ",prod
			listOfProducts.append(prod)
	print 	"list Of Products: ",listOfProducts			
	#print "max of row wise products:", max(listOfProducts)
	return max(listOfProducts)



	
def getColumnWiseProduct(Matrix,prodlen):	
	# Column wise product
	print "Column wise product"
	listOfProducts = []
	beg = 0
	end = 0
	for i in range(0,len(Matrix)): # i is the column number
		# first extract each column from the matrix.
		eachCol = [row[i] for row in Matrix] 
		print eachCol
		for j in range(0,(len(eachCol)-(prodlen-1))): 
			prod = 1
			beg = j
			end = j+prodlen
			for k in range(beg,end):
				prod = prod*eachCol[k]
				print prod
			listOfProducts.append(prod)
	print 	"list Of Products: ",listOfProducts	
	#print "max of column wise products:", max(listOfProducts)
	return max(listOfProducts)

	


def getDiagonalWiseProduct(Matrix,prodlen):
	# Diagonal wise product
	print "Diagonal wise product"
	listOfProducts = []
	beg = 0
	end = 0
	diagonalNumList = [[]]
	d = -1
	# Extract all diagonal elements from the Matrix and store it in a list of lists
	for i in  range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			m = i
			n = j
			d = d+1
			while(m<5 and n<5):
				diagonalNumList[d].append(Matrix[m][n])					
				m = m+1
				n = n+1
				print diagonalNumList
	# Compute product of diagonal elements
	for i in range(0, len(diagonalNumList)):	
		for j in range(0,(len(diagonalNumList[i])-3)):
			prod = 1
			beg = j
			end = j+4
			for k in range(beg,end):
				prod = prod*diagonalNumList[i][k]
			listOfProducts.append(prod)												
	return max(listOfProducts)	
	
	

def readAllNumbers():
	matrix = [[0]*5 for i in range(5)]
	#print matrix
	f = open('Grid-1.txt','rU')
	i = 0
	for line in f:	
		strList = line.split(" ")
		#print strList
		#print len(strList)
		for j in range(0,len(strList)-1):
			matrix[i][j] = int(strList[j])
		i = i+1			
	f.close()
	#print matrix
	#print "Number of rows in matrix:",len(matrix)
	#print matrix[0]
	#max = getProduct(matrix)
	return matrix
	

def main():
	productLength = 3
	grid = readAllNumbers()
	#print grid
	#getRowWiseProduct(grid,productLength)
	#columnMatrix = getAllColumns(grid)
	#print columnMatrix
	#getColumnWiseProduct(grid,productLength)
	diagonalMatrix = getAllDiagonals(grid)
	print diagonalMatrix



if __name__ == "__main__":
	main()