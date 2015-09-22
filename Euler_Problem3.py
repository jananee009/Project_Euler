# Largest Prime Factor
# Problem Source: https://projecteuler.net/problem=3
# Approach: 1. Get all the factors for the given number 600851475143.
# 2. Identify which of the factors are prime. 
# 3. Identify the largest number among the prime factors to get the desired number.

import math
import time

# this method returns a list of all factors for the given number.
def getFactors(number):
	# if the square root of the given number is prime, then that number is the highest prime factor. 
	sqrt = int(round(math.sqrt(number)))
	if checkForPrime(sqrt):
		return sqrt
	else:	
		# create a list of all numbers that evenly divide the given number. 
		factors = []
		# since the given number 600851475143 is odd, it wont be divisible by 2 or any even number. 
		# So, we will start checking from number 3 and increment by 2. 
		for i in range(3,sqrt+1,2):  
			if number % i == 0:
				factors.append(i)
	return factors		

# this method takes a list of numbers  and returns the highest prime number in the list.
def getPrimeFactors(factlist):	
	for i in reversed(factlist):					
		flag = checkForPrime(i)
		if(flag):
			return i
	
# This method checks whether a given number is prime.	
def checkForPrime(number):
	listOfFactors = []
	if number == 2:
		return True
	else:		
		for i in range(1,number+1):
			if number % i == 0:
				listOfFactors.append(i)
	if len(listOfFactors)==2 and listOfFactors[0]==1 and listOfFactors[1]==number:
		return True
	else:
		return False	
			
				
		

def main():
	start_time = time.time()
	print "Calling function........"
	num = 600851475143
	factors = getFactors(num)
	if (type(factors) == int):
		print "The highest prime factor of 600851475143 is: ", factors
	elif ( type(factors) == list and len(factors) > 1):
		primeFactor = getPrimeFactors(factors)
		print "The highest prime factor of 600851475143 is: ", primeFactor
	print"Problem solved in %s seconds " % (time.time()-start_time)
	

if __name__ == "__main__":
	main()
	

	
	

	