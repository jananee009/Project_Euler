# Sum Square Difference
# Problem Source: https://projecteuler.net/problem=6
# Approach: First compute the sum of square of first 100 natural numbers.
# 2. Compute the sum of first 100 natural numbers and then square the sum. 
# 3. Compute the difference between the numbers computed in step 1 and step 2 to get desired result.

import time


def sumSquareDifference(n):
	sumofSquares = 0
	squareofsum = 0
	# compute the sum of squares of first n numbers.
	for i in range(1,n+1):
		sumofSquares = sumofSquares+i*i
	
	# compute the square of the sum of first n numbers:	
	sumOfFirst100Numebrs = 	n*(n+1)/2
	squareofsum = sumOfFirst100Numebrs * sumOfFirst100Numebrs
	
	# compute difference
	diff = squareofsum - sumofSquares
	
	return diff




def main():
	start_time = time.time()
	difference = sumSquareDifference(100)
	print "difference is: ",difference
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
	 
	


if __name__ == "__main__":
	main()


# Answer: 	25164150