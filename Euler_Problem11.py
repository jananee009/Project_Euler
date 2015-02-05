# Greatest product in a 20*20 grid

import numpy

def getProduct(Matrix):
	listOfProducts = []
	beg = 0
	end = 0
	# row wise product
	
	print "row wise product" 	
	for i in range(0,len(Matrix)):
		print "processing row:",i
		for j in range(0,(len(Matrix[i])-3)):
			prod = 1
			beg = j
			end = j+4
			#print "beg is:", beg
			#print "end is:", end
			for k in range(beg,end):
				prod = prod * Matrix[i][k]
			listOfProducts.append(prod)		
	#print "max of row wise products:", max(listOfProducts)
	
	
	#Column wise product
	print "Column wise product"
	for i in range(0,len(Matrix)):
		eachRow = [row[i] for row in Matrix]
		print eachRow
		for j in range(0,(len(eachRow)-3)):
			prod = 1
			beg = j
			end = j+4
			for k in range(beg,end):
				prod = prod*eachRow[k]
			listOfProducts.append(prod)
	print 		listOfProducts[17]
	print "max of column wise products:", max(listOfProducts)
	
	'''		
	# Diagonal wise product
	print "Diagonal wise product"
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
	'''
	

def readAllNumbers():
	matrix = [[0]*20 for i in range(20)]
	f = open('grid.txt','rU')
	i = 0
	for line in f:	
		strList = line.split(" ")
		for j in range(0,len(strList)):
			matrix[i][j] = int(strList[j])
		i = i+1			
	f.close()
	#print matrix
	#print "Number of rows in matrix:",len(matrix)
	#print matrix[0]
	max = getProduct(matrix)
	return max
	

def main():
	#greatestProd = readAllNumbers()	
	#print greatestProd
	readAllNumbers()




if __name__ == "__main__":
	main()