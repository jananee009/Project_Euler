# Problem 44: Pentagon Numbers	
# Problem Source: https://projecteuler.net/problem=44


import math
import time


def addSubtractPentagonalNumbers():
	i = 1
	n = 0
	m = 0
	while (True):
		i = i+1
		n = i*(3*i-1)/2
		for j in range(i-1,0,-1):
			m = j*(3*j-1)/2
			if(isPentagonal(n+m) and isPentagonal(n-m)):
				return n-m


# checks if a given number is pentagonal.
def isPentagonal(number):
	x = 0.0
	x = (math.sqrt(24*number+1)+1)/6 # from pentagonal numbers wikipedia page
	if ((x).is_integer()):
		return True
	else:
		return False	

	

def main():
	start_time = time.time()
	print "Difference between a pair of pentagonal numbers, whose sum and difference are pentagonal is: ", addSubtractPentagonalNumbers()
	print"Solution found  in %s seconds. " % (time.time()-start_time)
	
	

if __name__ == "__main__":
	main()	


# Answer: 5482660
