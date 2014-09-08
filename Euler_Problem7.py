# 10,001st Prime
import math

def getPrimeNumbers(n):
	primeNumbersList = []
	number = 2
	while(len(primeNumbersList) <> n):
		if(checkForPrime(number)):
			primeNumbersList.append(number)
		#print primeNumbersList
		number = number+1
		for i in range(0,len(primeNumbersList)):
			if(number % primeNumbersList[i] == 0):
				number = number + 1
				break					
	return 	primeNumbersList[n-1]		
				
		
		


def checkForPrime(num):
	#print "Checking For Prime"
	#print num
	primeList = []
	if( num == 2 or num == 3):
		return True
	else:
		sqrt = 	int(math.sqrt(num))
		for i in range(2,sqrt+1):
			if ((num % i)==0):
				primeList.append(i)
	if( len(primeList) == 0 ):
		return True
	else:
		return False	 			
				
				


def main():
	index = 10001
	primeNumber = getPrimeNumbers(index)
	print primeNumber
	


if __name__ == "__main__":
	main()