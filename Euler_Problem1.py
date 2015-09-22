# Problem 1: Multiples of 3 and 5
# Problem Source: https://projecteuler.net/problem=1
# Approach: Starting from 1, check whether a number is a multiple of 3 or 5. 
# Keep adding all the multiples until you reach the number 1000.


import math
import time

def getMultiplesOf3or5(limit):
	sumOfAllMultiples = 0 
	# From 1 going up to 1000, check whether the number is a multiple of 3 or 5.
	for i in range(1,1000):
		if (i%3==0 or i%5==0):
			sumOfAllMultiples = sumOfAllMultiples+i # compute sum of numbers that are multiples of 3 or 5.
	return sumOfAllMultiples		



def main():
	start_time = time.time()
	print "Calling function........"
	total = getMultiplesOf3or5(1000)
	print "Sum of all multiples of 3 or 5 under 1000 is: ",total
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	


# Answer: 233168	