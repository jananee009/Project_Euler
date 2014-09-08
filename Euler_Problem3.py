# Largest Prime Factor
import math

def getFactorsLessThansqrt(number):
# Optimize this method. Mathematically, there should be a better way of getting factors.
	sqrt = int(round(math.sqrt(number)))
	if checkForPrime(sqrt):
		return sqrt
	else:	
		factors = []
		for i in range(2,sqrt+1):
			if number % i == 0:
				factors.append(i)
	return factors		

def getPrimeFactors(factlist):	
	for i in reversed(factlist):					
		flag = checkForPrime(i)
		if(flag):
			return i
	
	
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
	num = 600851475143
	#600851475143
	factors = getFactorsLessThansqrt(num)
	print factors
	if (type(factors) == int):
		print factors
	elif ( type(factors) == list and len(factors) > 1):
		primeFactor = getPrimeFactors(factors)
		print primeFactor
	
	

if __name__ == "__main__":
	main()
	

	
	

	