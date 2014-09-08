# Summation of primes below 2 million

import math

def generatePrimeList():
	sum = 5
	i = 5
	limit = 2000000
	while (i<limit):
		if(checkForPrime(i)):
			sum = sum+i
		i = i+2
		if ( i < limit and checkForPrime(i)):
			sum = sum+i
		i = i+4	
	return sum		
		
	

def checkForPrime(num):	
	if (num == 2):
		return True
	else:	
		factorList = []
		sqrtNum = int(math.sqrt(num))
		for i in range(2,sqrtNum+1):
			if ( num % i == 0 ):
				factorList.append(i)		
		if ( len(factorList)==0):
			return True
		else:
			return False							


def main():
	sum = generatePrimeList()
	print sum	
	#a = checkForPrime(4)
	#print a

if __name__ == "__main__":
	main()