# Problem 46: Goldbach's Other Conjecture
# Problem Source: https://projecteuler.net/problem=46
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# Approach: 1. Start processing from 35. Let us call it n. 
# 2. Check if n is composite.
# 3. if n is composite, as per the problem statement, we can express n as n = primenumber + 2*(y)(y). So, primenumber < n and y = {1,2,3,......}
# The primenumber and y are unknowns in the above equation. We can rewrite above equation as:  primenumber = n - 2*(y)(y)
# 4. Compute n - 2*(y)(y) by substituting y as {1,2,3,....} each time. For each value check it is prime. 
# 5. If the value is prime, go to next value of n and repeat steps 2 to 5.
# 6. If the value is negative, then n is our desired result.


import math
import time

listOfPrimes = [2,3,5,7,11,13,17,19,23,29,31,37]

def disproveGoldbachOtherConjecture():
	n = 35	# Using the info given in the problem statement, we start checking from 35.
	while(True):
		n = n+2	
		if (not isPrime(n)): #check whether n is composite 
			for y in range(n): # for each y 
				value = n - 2*y*y # compute value
				if(value < 0):
					return n
				elif (isPrime(value)): # check if value is prime
					break

def isPrime(number):
	if number in listOfPrimes:
		return True
	sqrt = int(math.sqrt(number))
	for i in range(2,sqrt+1):
		if (number % i == 0):
			return False 
	listOfPrimes.append(number)
	return True		

	

def main():
	start_time = time.time()
	print "The smallest odd composite that CANNOT be written as the sum of a prime and twice a square is: ", disproveGoldbachOtherConjecture()
	print"Solution found  in %s seconds. " % (time.time()-start_time)


if __name__ == "__main__":
	main()	


# Answer: 5777
