

import math

class SieveOfEratosthenes:
	def __init__(self):
		self.listOfNumbers = []


	# checks if a given number is prime or non prime.
	def isPrime(self,num):
		sqrtNum = int(math.sqrt(num))
		for i in range(2,sqrtNum+1):
			if num % i == 0:
				return False
		return True		
	
	# Returns a list of all prime numbers under a certain number.	
	def implementSieveOfEratosthenes(self,limit):
		listOfPrimes = []
		self.listOfNumbers = [True]*(limit+1)
		# create a list of booleans. Initially we assume that all numbers are prime. Hence their values are set to True. 
		self.listOfNumbers[0:2] = [False,False] # Since 0 and 1 are not prime numbers, set the flag for them as False in the list of booleans. 
		index = 2
		sumOfPrimes = 0
		while (index < limit**0.5+1):
			if(self.isPrime(index)): # if index is prime, generate all the multiples of the index below limit and set their corresponding values to False. 
			# i.e. once we have found a prime number, we  find all its multiples(composite numbers) and cross them off our list.			
				for i in range(index,limit/index+1):
					self.listOfNumbers[index*i] = False

			# Get the next highest value of index from the list whose value is True.	
			for  j in range(index+1,limit+1):
				if(self.listOfNumbers[j]):
					index = j
					break			

		# find the sum of all indices that have been marked as True on the list.			
		for ind,val in enumerate(self.listOfNumbers):
			if(val):
				listOfPrimes.append(ind)			
		return listOfPrimes		








