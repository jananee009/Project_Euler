# what is the 10,001st Prime number?
# Problem Source: https://projecteuler.net/problem=7
# Approach:  Starting from 2,  write all prime numbers that you know sequentially to a list. 
# Since a prime number is odd, increment the last  prime number added to the list by 2 and check if the new number is prime. 
# Add the number to the list if it is prime, else add 2 to the number and check if it is prime. 
# Repeat this process until you have added 10,001 prime numbers to the list.
# The 10,001st number added to the list is the required answer.

import math
import time

#  creates a list prime numbers sequentially and returns the 10,001st prime number.
def getPrimeNumbers(n):
	primeNumbersList = [2,3,5,7,11,13,17,19] # add as many  prime numbers you know sequentially to a list.
	number = 23
	while(len(primeNumbersList) != n):
		if(checkForPrime(number)): 
			primeNumbersList.append(number)

		number = number+2			
	return 	primeNumbersList[n-1]		
				
				

# checks if a given number is prime. 
def checkForPrime(num):
	factorList = []
	sqrt = 	int(math.sqrt(num))
	for i in range(2,sqrt+1):
		if ((num % i)==0):
			factorList.append(i)
	if( len(factorList) == 0 ):
		return True
	else:
		return False	 			
				
				

def main():
	start_time = time.time()
	print "Calling function........"
	index = 10001
	primeNumber = getPrimeNumbers(index)
	print primeNumber
	print"Problem solved in %s seconds " % (time.time()-start_time)
	


if __name__ == "__main__":
	main()

# Answer: 104743	