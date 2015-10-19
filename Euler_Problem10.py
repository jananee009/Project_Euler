# Summation of primes below 2 million
# Problem Source: https://projecteuler.net/problem=10
# Approach: Implement sieve of Eratosthenes to generate prime numbers under 2,000,000
# Then sum all the prime numbers to get result.


import math
import time
import SieveOfEratosthenes as soe
	


def main():
	start_time = time.time()
	maxLimit = 2000000
	mySoE = soe.SieveOfEratosthenes()
	primeList = mySoE.implementSieveOfEratosthenes(maxLimit)
	print "The sum of all primes under",maxLimit,"is:",sum(primeList)	
	print "Time taken to solve the problem: ", (time.time()-start_time), " seconds."


if __name__ == "__main__":
	main()

# Answer: 142913828922	