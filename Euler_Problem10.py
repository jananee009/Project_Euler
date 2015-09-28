# Summation of primes below 2 million
# Problem Source: https://projecteuler.net/problem=10
# Approach: Implement sieve of Eratosthenes to generate prime numbers under 2,000,000


import math
import time
	

def sieveOfEratosthenes(limit):
	listOfNumbers = [True]* (limit+1) # create a list of booleans. Initially we assume that all numbers are prime. Hence their values are set to True. 
	listOfNumbers[0:2] = [False,False] # Since 0 and 1 are not prime numbers, set the flag for them as False in the list of booleans. 
	index = 2
	sumOfPrimes = 0
	while (index < limit**0.5+1):
		if(checkForPrime(index)): # if index is prime, generate all the multiples of the index below limit and set their corresponding values to False. 
		# i.e. once we have found a prime number, we  find all its multiples(composite numbers) and cross them off our list.			
			for i in range(index,limit/index+1):
				listOfNumbers[index*i] = False

		# Get the next highest value of index from the list whose value is True.	
		for  j in range(index+1,limit+1):
			if(listOfNumbers[j]):
				index = j
				break

	# find the sum of all indices that have been marked as True on the list.			
	for ind,val in enumerate(listOfNumbers):
		if(val):
			sumOfPrimes = sumOfPrimes + ind
	return sumOfPrimes		


				

	
	
# this method determines if a given number is prime.
def checkForPrime(num):	
	sqrtNum = int(math.sqrt(num)) 
	for i in range(2,sqrtNum+1): # to check if an input is prime, you have to check only until its square root, instead of checking every number less than the input.
		if ( num % i == 0 ): # if a number divides the input completely, then the input cannot be prime.  
			return False				
	return True							


def main():
	start_time = time.time()
	maxLimit = 2000000
	sumOfPrimeNumbers = sieveOfEratosthenes(maxLimit)
	print "The sum of all primes under",maxLimit,"is:",sumOfPrimeNumbers	
	print "Time taken to solve the problem: ", (time.time()-start_time), " seconds."


if __name__ == "__main__":
	main()

# Answer: 142913828922	