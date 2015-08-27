# Problem 37: Truncatable Primes
# Approach: Use brute force approach. 
# 1. Generate prime number. 
# 2. Check whether each prime number is truncatable. 
# 3. Keep repeating steps 1 and 2 until we have 11 truncatable primes.
# The main bottleneck is in the method for generating prime numbers. 

import math
import time



def checkTruncatable(primeNumber,set_of_primes):
	#Truncate number by removing each digit starting from right most end and check if resulting number is prime.
	length = len(str(primeNumber)) # get the length of the prime number	
	num_right_to_left = primeNumber
	for i in range(1,length):
		num_right_to_left = num_right_to_left / 10
		if (num_right_to_left not in set_of_primes):
			return False
					
	#Truncate number by removing each digit starting from left most end and check if resulting number is prime.
	num_left_to_right = primeNumber
	power = length-1
	while(power >= 1):
		num_left_to_right = num_left_to_right % (10**power)
		if (num_left_to_right not in set_of_primes):
			return False
		power = power - 1

	return True		



def checkForPrime(number):
	factors = []
	for i in range(2,int(math.sqrt(number))+1):
		if (number % i == 0):
			factors.append(i)
	if (len(factors) == 0):
		return True
	else:
		return False



def findTruncatablePrimeSum(maxLimit):
	primeNumbers = [2,3,5,7]
	primeNumbers = set(primeNumbers)
	truncatablePrimes = []
	n = 11 # starting point for finding truncatable primes
	while(len(truncatablePrimes) < maxLimit):
		if(checkForPrime(n)): # check if number is prime
			primeNumbers.add(n) # if prime, add number to the list of prime numbers 
			if(checkTruncatable(n,primeNumbers)): # check if prime number is truncatable
				truncatablePrimes.append(n) # if truncatable, add number to list of truncatable primes
		n = n+1		
	print truncatablePrimes
	return sum(truncatablePrimes) 						

		


def main():
	start_time = time.time()
	print "Calling function........"
	truncatablePrimeSum = findTruncatablePrimeSum(11)
	print "The sum of the only eleven primes that are both truncatable from left to right and right to left: ",truncatablePrimeSum
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	


# Answer: 748317
# Problem solved in 64.9540538788 seconds	