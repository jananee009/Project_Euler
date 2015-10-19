# Consecutive Prime Sum
# Problem Source = https://projecteuler.net/problem=50
# Which prime, below one-million, can be written as the sum of the most consecutive primes?


import time
import math
import SieveOfEratosthenes as soe

def findConsecutivePrimeSum(primeList):
	primeDict = {} # stores the prime number as key and its  number of  consituent consecutive primes that add up to it as value.
	for prime in reversed(primeList): # start from the end of the prime numbers list.
		sum = 0
		index = -1
		while (sum < prime): # keep adding consecutive primes starting from 2 until the sum equals or exceeds the prime number.
			index += 1
			sum = sum + primeList[index]		
		if (sum == prime): # if the sum of consecutive prime numbers equal the given prime number, 
			primeDict[prime] = index+1 # store the prime number and number of consecutive primes  that were added in to the dictionary as key,value pair. 
		elif (sum > prime): # if the sum exceeds the prime number, get the difference and check if the difference can be expressed as sum of first n consecutive numbers.
			difference = sum - prime
			newSum = 0
			count = 0
			for p in primeList:
				newSum = newSum + p
				count += 1
				if (newSum == difference): # if the difference can be expressed as sum of first n consecutive numbers
					primeDict[prime] = (index+1)-count # subtract n from the number of primes that were added  previously.
					break
				elif (newSum > difference): # if the difference CANNOT be expressed as sum of first n consecutive numbers
					break # process the next highest prime number in the list. 
	
	# Get the prime number from the dictionary that has the highest value
	v = list(primeDict.values())
	k = list(primeDict.keys())	
	return k[v.index(max(v))]



def main():

	start_time = time.time()	
	maxLimit = 1000000
	
	# first generate all prime numbers under 1000000 by using Sieve Of Eratosthenes.
	mySoE = soe.SieveOfEratosthenes()
	primes = mySoE.implementSieveOfEratosthenes(maxLimit)

	print "The prime, below one-million, that can be written as the sum of the most consecutive primes is: ",findConsecutivePrimeSum(primes)
	print"Problem solved in %s seconds " % (time.time()-start_time)




if __name__ == "__main__":
	main()

# Answer: 997651