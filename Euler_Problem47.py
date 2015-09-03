# Problem 47: Distinct Prime Factors
# Approach: 1. For each number generate all prime factors. 
# 2. Store all prime factors in a set. This way we will store each prime factor at most once. 
# 3. Check if the set has 4 elements. (i.e. here we check if the number has 4 distinct prime factors.)
#	 a) if no, go to step 1 to process next number. 
# 	 b) if yes:
#		i) Store the number in a list. Perform steps 1 to 3 for the next 3 consecutive numbers.
#		ii) If any of the 3 consecutive numbers do not have 4 distinct primes, empty the list.
#       iii) go to step 1 to process the next number. 

import math
import time
			

def getDistinctPrimes(c):

	# Instead of starting our search from 1, We will start our search from the number 210. 
	# Since we want 4 distinct prime factors for a number, the smallest number with 4 distinct prime factors is 2*3*5*7 = 210
	number = 210
	consecutiveNums = []  # stores the 4 consecutive numbers that each have 4 distinct prime factors.
	while(len(consecutiveNums) != c):

		# check if a given number has 4 distinct prime factors
		if(is4DistinctPrimes(number,c)): 

			# store that number in to the list.
			consecutiveNums.append(number)

			# check if the next 3 numbers each have 4 distinct prime factors.  
			for i in range(1,c):
				number = number + 1
				if(is4DistinctPrimes(number,c)):
					consecutiveNums.append(number)
				else: # if any of the next 3 numbers do not satisfy the condition: empty the list, get out of the for loop and process the next number. 
					consecutiveNums = []
					break				
		number = number + 1	
	return 	consecutiveNums
	
					



	
# checks whether the number k has p number of distinct prime factors. Here p = 4.
def is4DistinctPrimes(k,p):
	setOfPrimes = set()	
	
	# get all the distinct prime factors of a number.
	setOfPrimes = set(getPrimeFactors(k))
	
	if (len(setOfPrimes)) == p:
		return True
	else:
		return False	 
	

def getPrimeFactors(num):
	factorList = []
	
	# get all the 2s that can divide the number.
	while(num%2 == 0):
		factorList.append(2)
		num = num/2

	# at this point n must be odd.
	sqrt = 	int(math.sqrt(num))
	for i in range(3,sqrt+1,2):	
		while (num%i==0):
			#print i
			factorList.append(i)
			num = num/i

	if(num>2):
		factorList.append(num)	

	return factorList
	

			
		
	
def main():
	
	start_time = time.time()
	print "Calling function........"
	requiredList = getDistinctPrimes(4)
	print "4 Consecutive numbers with 4 distinct prime factors: ",requiredList
	print"Time taken: ", (time.time()-start_time) , "seconds."
	


		
	

if __name__ == "__main__":
	main()	
	
	
