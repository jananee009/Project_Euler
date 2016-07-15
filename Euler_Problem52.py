# Permuted multiples
# Problem Source: https://projecteuler.net/problem=52
# Approach
# 1. Find values of x that we need to process. 
	# dont check for each number x whether x, 2x, 3x, 4x, 5x, 6x have the same digits, but in different order.
	# we can  ignore single digit numbers.	
	# Starting from 10, We need not process each number to find the required answer. 
	# For 2-digit numbers, range of x will not be up to 99. 
	# Since 6x must also be a 2-digit number (to be a  permuted multiple of x), the maximum value of 6x can be 99. i.e. x = 99/6 = 16.
	# Therefore, for 2-digit numbers, range for x is 10 <= x <= 16. If x = 17, 6x = 102. Thus x and 6x cannot be permutations of each other.
	# Similarly, we can compute the range for 3-digit, 4-digit, 5-digit, numbers and so on. 

# 2. For each x, compute multiples and check if multiples are permutations of each other

# 3. Once we find the x such that x, 2x, 3x, 4x, 5x, 6x are permutations of each other, return result.  

import math
import time


def findRanges():
	ending_point = 9
	result = -1 # initial
	while(True):
		if (result < 0):
			# compute range of x
			starting_point  = ending_point + 1
			ending_point = (10 * starting_point) - 1
			actual_end_point =  ending_point / 6 
			

			result = findPermutedMultiples(starting_point,actual_end_point)
		else:
			return result	


# find all multiples for each number x within the range and check whether x, 2x, 3x, 4x, 5x, 6x are all permutations of each other.
# if suitable x not found, then return -1.
def findPermutedMultiples(start, end):
	while(True):
		for x in range(start,end+1):
			
			# for each value of x, find x, 2x, 3x, 4x, 5x, 6x
			multiples = [ x*i for i in range(1,7)] 
			
			# find if the multiples are permutations of each other.
			a = set(str(multiples[0]))
			b = set(str(multiples[1]))
			c = set(str(multiples[2]))
			d = set(str(multiples[3]))
			e = set(str(multiples[4]))
			f = set(str(multiples[5]))
			if a == b == c == d == e == f: 
				return x	
		return -1


def main():
	start_time = time.time()
	print findRanges()
	print"Problem solved in %s seconds " % (time.time()-start_time)

	

if __name__ == "__main__":
	main()


# Answer: 142857	