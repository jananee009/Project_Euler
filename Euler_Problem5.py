# Smallest Multiple

import math

def getPrimeFactors(number):
	primefactorslist = []
	sqrt = int(math.sqrt(number))
	for i in range(2,sqrt+1):
		if(number % i == 0):
			if(checkForPrime(i)):
				primefactorslist.append(number)
	return 	primefactorslist		
				
				

def checkForPrime(num):
	listOfFactors = []
	if (num == 2):
		return True
	else:
		for i in range(1,num+1):
			if (num % i == 0):
				listOfFactors.append(i)
	if ( len(listOfFactors) == 2 and listOfFactors[0] == 1 and listOfFactors[1] == 2 ):
		return True						
	else:
		return False
		
def doPrimeFactorization(dividend,listOfPrimes):	
	for j  in range(0,len(listOfPrimes)):
		number = dividend
		power = 0
		remainder = 0
		quotient = 0
		while (remainder == 0):
			quotient = number / listOfPrimes[j]
			remainder = number % listOfPrimes[j]	
			if ( remainder == 0 ):
				power = power + 1
				number = quotient
			
		
		
			
				
def checkDivisibility(dividend, divisor):
	if( dividend % divisor == 0 ):
		return dividend / divisor
	else:
		return -1	



def main():
	primeFactors = 	getPrimeFactors(20)
	


if __name__ == "__main__":
	main()