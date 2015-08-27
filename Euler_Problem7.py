# what is the 10,001st Prime number?
import math
import time

def getPrimeNumbers(n):
	primeNumbersList = [2,3]
	number = 5
	while(len(primeNumbersList) != n):
		if(checkForPrime(number)):
			primeNumbersList.append(number)
		#print primeNumbersList
		number = number+2				
	return 	primeNumbersList[n-1]		
				
		
		


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