# Prime Permutation
# Problem Source = https://projecteuler.net/problem=49
# Arithemetic sequence made up of three 4-digit numbers in increasing sequence such that 
# (i) each number is prime 
# (ii) each of the 4-digit numbers are permutations of one another.
# (iii) each term increases by same constant x to give the next number.
# What 12-digit number do you form by concatenating the three numbers in this sequence?
# Approach:
# 1. Get all 4-digit primes.
# 2. Take 2 primes p1 and p2. Calculate difference = p1 - p2. Calculate n = p2 + difference
# 3. Check if n is prime and n < 10000. if yes, go to step 4 else go to step 2.
# 4. Check if p1, p2, n are permutations of each other. If yes, go to step 5 else go to step 2.
# 5. Answer found. p1, p2, n is the required Arithemetic sequence. 



import time
import math
import SieveOfEratosthenes as soe
import itertools 




# determines if the numbers in a list are permutations of each other.
def checkIfPermutationsOfEachOther(list_of_three):
	a = [ int(i) for i in str(list_of_three[0])] # split number to digits  
	b = [ int(j) for j in str(list_of_three[1])]
	c = [ int(k) for k in str(list_of_three[2])]
	if (sorted(a) == sorted(b) == sorted(c)):
		return True
	return 	False	




def findPrimePermutationSequence():
	#first generate all prime numbers under 10000 by using Sieve Of Eratosthenes.
	mySoE = soe.SieveOfEratosthenes()
	primes = mySoE.implementSieveOfEratosthenes(9999) # since we are interested only in 4 digit primes.
	fourDigitPrimes = [p for p in primes if p > 999] # get all 4 digit primes
	result = []

	for i in range(0, len(fourDigitPrimes)-1):
		for j in range(i+1, len(fourDigitPrimes)):
			difference = fourDigitPrimes[j] - fourDigitPrimes[i] # calculate difference between 2 primes.
			thirdNumber = fourDigitPrimes[j] + difference # compute third number
			list_of_three_numbers = list([fourDigitPrimes[i],fourDigitPrimes[j],thirdNumber]) 
			if (mySoE.isPrime(thirdNumber)): # check if third number is prime
				if (checkIfPermutationsOfEachOther(list_of_three_numbers)): # check if three numbers are permutations of each other
					result.append(list_of_three_numbers)

			if (len(result) == 2): # as per information given in the problem
				return	result[1]	

	 		

def main():

	start_time = time.time()	
	three_prime_numbers = findPrimePermutationSequence()
	answer = ""
	for p in three_prime_numbers:
		answer = answer + str(p)
	print "The 12-digit number formed by concatenating the three terms is", int(answer)
	print"Problem solved in %s seconds " % (time.time()-start_time)




if __name__ == "__main__":
	main()

# Answer: 296962999629