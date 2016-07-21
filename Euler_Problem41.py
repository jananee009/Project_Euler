# pandigital primes
# Problem 41: https://projecteuler.net/problem=41
# What is the largest n-digit pandigital prime that exists?
# Approach: 1. Since we are looking for the largest panditial prime number, let us start our search from the higher end. 
# 2.But, we know that our pandigital number cannot be 9 digits long because such a number would be divisible by either 2, 3 or 5 and hence it cannot prime. 
# [Use n*(n+1)/2). The result will always be divisible by 3.]
# 3.For the same reasons, our pandigital prime number cannot be 8-digit, 6-digit or 5-digit long. 
# 4.But, our pandigital prime number may be 7 digits long or 4 digits long. So, we can start searching for prime numbers in 7 digit pandigital primes.
# 5.If we dont find any, we can search among 4 digit pandigital numbers. 
# 6.We can generate 7 digit pandigital numbers using permutations. The units digit of the 7 digit cannot be in (0,2,4,5,6,8). So, we can fill the units position with (1,3,7,9) or 4 ways.
# We will fill the left most position with 7 ( since we want to start at the higher end here). The remaining 5 positions in the middle can be filled in 5! ways. 
# So,we will have 1*5!*4 = 480 numbers. If we are unable to find a 7 digit pandigital prime starting with 7, we will search for one starting with 6 and we will keep going. 

import math
import time
import Common
from itertools import permutations



			
def findLargestPandigitalPrime():
	largestPrime = 0

	# find 7 digit pandigital prime:
	validUnitsDigit = [1,3] # the units digit of a 7 digit pandigital prime number cannot be 9. It cannot be 7 either because we are checking for 7 digit numbers beginning with 7.
	for digit in validUnitsDigit:
		inputString = "" # the 5 digit number to be permuted will be input in the form of a string to the permutations method.
		# Form the pandigital input string based on the units digit being considered.
		for i in range(1,7):
			if i != digit:
				inputString = inputString + str(i)
		perms = [int('7'+''.join(p)+str(digit)) for p in permutations(inputString)]	# Append 7 to the beginning of all permutations and the units digit to the end. So we have all permutations starting with 7 and ending with "units digit"
		perms.sort(reverse=True) # since we want the highest number, sort the list ind descending order.
		for p in perms:
			if (Common.isPrime(p) and p > largestPrime):
				largestPrime = p
				break			
	return largestPrime			

	
def main():
	start_time = time.time()
	print "The largest n-digit pandigital prime that exists is : ", findLargestPandigitalPrime()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 7652413 	
