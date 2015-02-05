# Problem 27: Quadratic primes

import math
import time
			

def generatePrime():
	print "Inside function......"
	a_values = []
	b_values = []
	prime_count = []
	# get the total number of primes for all combination of values for a and b
	for a in range(-1000,1000):
		for b in range(-1000,1000):			
			numberOfPrimes = 0
			
			n = 0			
			if(b<0 and n==0) or (b%2==0 and n==0):
				pass
			else:
				flag = True
				while(flag):
					quad_eqn = (n*n)+(a*n)+(b)
					if(quad_eqn>0):
						flag = isPrime(quad_eqn)
						if(flag):
							numberOfPrimes = numberOfPrimes+1
							n = n+1
					else:
						flag = False		
				a_values.append(a)
				b_values.append(b)
				prime_count.append(numberOfPrimes)		
	# Now find the a and b that have the highest number of primes	
	print "Maximum number of prime numbers generated is: ",max(prime_count)
	index = prime_count.index(max(prime_count))	
	reqd_a = a_values[index]
	reqd_b = b_values[index]
	print "required values of a and b are: ",reqd_a, "and ",reqd_b
	return		



def isPrime(number):
	if	(number == 2 or number == 3):
		return True 	
	elif (number < 2 or number%2==0):
		return False	
	else:
		maxRange = int(math.sqrt(number))
		for i in range(3,maxRange+1):
			if(number%i == 0):
				return False
			else:
				pass
	return True				
		
	
def main():
	start_time = time.time()
	print "Calling function........"
	generatePrime()
	print"Time taken: ", (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	
	
# Solution:
# Maximum number of prime numbers generated is:  71
# required values of a and b are:  -61 and  971	
	
		
		
		
		
	