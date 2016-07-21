# Smallest Multiple
# Problem Source: https://projecteuler.net/problem=5


import math
import time
import Common



def findSmallestMultiple():
	to_be_multiplied = [] # list of numbers to be multiplied to get the smallest multiple i.e. the result	
	for number in range(2,21):
		prime_fact_list = Common.findPrimeFactors(number) # express the number in terms of its prime factors
		prime_factor_count = {fact:prime_fact_list.count(fact) for fact in prime_fact_list } # keep a count of the number of times a prime number appears as a factor for a number
		for key in prime_factor_count: 
			if key not in to_be_multiplied: # check if the prime factor is already in the to_be_multiplied list. If not, add it. 
				to_be_multiplied.append(key)
			else:
				if 	prime_factor_count[key] > to_be_multiplied.count(key):
					to_be_multiplied.append(key)
	return Common.computeProductOfAList(to_be_multiplied)				



def main():
	start_time = time.time()
	print findSmallestMultiple()
	print"Problem solved in %s seconds " % (time.time()-start_time)

	

if __name__ == "__main__":
	main()


# Answer: 232792560	
# Problem solved in 0.000252962112427 seconds 