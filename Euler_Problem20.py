# Factorial digit sum
# Problem 20: https://projecteuler.net/problem=20
# Find the sum of the digits in the number 100!
# Approach: Compute 100!. Get digits of the result. Sum the digits to obtain result.


import math
import time
import Common

common = Common.Common()

# returns the factorial of a number			
def computeFactorial(n):
	if (n==1 or n==0):
		return 1
	return n*computeFactorial(n-1)	

	
def main():
	start_time = time.time()
	print "The sum of the digits in the number 100!: ", sum(common.getDigits(computeFactorial(100)))
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 648	
