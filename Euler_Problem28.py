# Problem 28: Number Spiral Diagonals
# Approach: We will create a list that will contain all the numbers that will be present on the diagonal of a n*n square. 
#Look at the given 5*5 (n*n) diagonal. If you observe the numbers on the diagonal, we can see a pattern. 
#  There are concentric squares in a n*n number spiral and each square has 4 corners that will lie on the diagonal.



import math
import time
			

def findSpiralDiagonalSum(dimension):
	diagonalNumberList = findNumbersOnSpiralDiagonal(dimension)
	spiralDiagonalSum = sum(diagonalNumberList)
	return spiralDiagonalSum




def findNumbersOnSpiralDiagonal(n): # returns a list of all numbers that would be on the diagonal of a n*n spiral.
	spiralDiagonalNumbers = []
	factor = n-1
	diagonalNumber = n*n # This will be highest number in the diagonal
	spiralDiagonalNumbers.append(diagonalNumber)
	while(factor >= 2 and diagonalNumber >0):
		for i in range(1,5):
			diagonalNumber = diagonalNumber-factor
			spiralDiagonalNumbers.append(diagonalNumber)
		factor = factor-2	
	return spiralDiagonalNumbers	


	


			
		
	
def main():
	start_time = time.time()
	requiredSum = findSpiralDiagonalSum(1001)
	print "the sum of the numbers on the diagonals in a 1001 by 1001 spiral is: ",requiredSum
	print"Time taken: ", (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	
	
# Answer: 669171001
# Time taken:  0.00421810150146 seconds		
		
		
		
	