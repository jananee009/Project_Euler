# Prime Pair Sets
# Problem 60: https://projecteuler.net/problem=60
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
# Approach: 1. In this problem we need to find 5 prime numbers such that when we pick any 2 numbers among them and concatenate, we get another prime number.  
# 3. We will solve the problem using brute force. 
# 4. a) First generate a list of prime numbers, say under 1000. 
# b) From the above master list of primes, take 5 consecutive primes, concatenate to see if the above condition is satisfied. If not, delete a prime and take the next
# prime from the master list and do the process. 
# 5. One challenge in this problem is to identify which prime number(s) to skip.
# 6. For e.g. we can easily identify that we must skip 2 and 5 because we know that any number ending in 2 or 5 cannot be a prime number. 
# 7. But consider the following set of primes [3,7,11,13,17]. We will generate 20 numbers by concatenating these 5 primes. The list is below:
# 8. [37,73,311,113,313,133,317,173,711,117,713,137,717,177,1113,1311,1117,1711,1317,1713]
# 9. Consider 3 and 13. We can form 313 and 133 by concatenating 3 and 13. 313 is prime but 133 is not. Now in this case, do we reject 13 or 3 ?


import math
import time
import Common
import SieveOfEratosthenes as soe


def findPrimePairSets():
	# first generate prime numbers using sieve of eratosthenes.
	#primeList = mySoE.implementSieveOfEratosthenes(1000)
	primeList = [3,7,11,13,17]
	primePairList = [] # will contain 5 prime numbers at a time.
	common = Common.Common()
	# skip 5. Any number ending in 5 is going to be non prime.
	# Skip 2. Any number ending in 2 is going to be non prime.
	for primeNum in primeList:
		# add 5 prime numbers to your prime pair list
		while len(primePairList) < 6:
			primePairList.append(primeNum)

		# create concatenations







	return	

		

	
def main():
	start_time = time.time()
	common = Common.Common()
	print common.isPrime(313)
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		

if __name__ == "__main__":
	main()	
	

# Answer:  	972
