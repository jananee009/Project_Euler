# Problem 35: Circular Primes
# Approach:
# First generate all prime numbers up to 1 million.
# Then generate ciruclar rotations for each prime number and check if each rotation is prime. 
# Return a list of circular primes. 
# The trickiest part in this problem is to implement the fastest way to generate all prime numbers up to 1000000 


import math
import time

def findPrimes(limit): # Returns a list of prime numbers below limit. 
	primeNumbersList = [2,3]
	number = 5
	while(number < limit):
		if(checkForPrime(number)):
			primeNumbersList.append(number)
		#print primeNumbersList
		number = number+2				
	return 	primeNumbersList	

			


def findCircularPrimes(number):
	allPrimes = findPrimes(number)	# get  all the primes under the given number
	print "Number of primes under 1 million: ",len(allPrimes)
	circularPrimes = []
	for i in range(0,len(allPrimes)):
		allRotationsPrime = True
		if (allPrimes[i] > 10):
			allRotations = getAllRotations(allPrimes[i])
			for j in range(0,len(allRotations)):
				if (not checkForPrime(allRotations[j])):
					allRotationsPrime = False
					break

		if (allRotationsPrime or (allPrimes[i]<10)):
			circularPrimes.append(allPrimes[i])	
	print "Circular Primes: ",	circularPrimes		
	return(len(circularPrimes))		




def checkForPrime(num): # returns True if input number is prime else returns false
	#print "Checking For Prime"
	#print num
	factorList = []
	sqrt = 	int(math.sqrt(num))
	for i in range(2,sqrt+1):
		if ((num % i)==0):
			factorList.append(i)
	if( len(factorList) == 0 ):
		return True
	else:
		return False	 



def getAllRotations(number): # returns a list of all circular rotations of a number.
	rotations = []
	list_of_digits = [i for i in str(number)] # convert number to digits and then to characters
	list1 = []
	for i in range(0,len(list_of_digits)-1):
		# remove first element from the list
		remove = list_of_digits.pop(0)
		# append this element to the end of the list.
		list_of_digits.append(remove)
		# convert list of characters to a single string of numbers
		str1 = ''.join(list_of_digits)
		rotations.append(int(str1))
	#print rotations
	return rotations




def main():
	start_time = time.time()
	print "Calling function........"
	count = findCircularPrimes(1000000)
	print "Total number of circular primes under 1 million is: ",count
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	