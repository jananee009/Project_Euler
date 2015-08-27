# Problem 23: Non-abundant sums
# Approach: First find a list of all abundant numbers that are under 28,124.
# Using this list, find all numbers under 28,124 that can be expressed as a sum of two abundant  numbers.
# Then we can find all numbers under 28124 that cannot be expressed as a sum of 2 abundant  numbers.


import math
import time


def findAllAbundantNumbers(): # Returns a list of all abundant numbers less than or equal to 28,123.
	abundantNumbers = []
	for n in range(2,28124):
		sumOfDivisors = sum(findProperDivisors(n))
		if (sumOfDivisors > n):
			abundantNumbers.append(n)			
	return 	abundantNumbers	




def findProperDivisors(number): # returns a list of proper divisors for a number.
	properDivisors = [1]
	for divisor in range(2, int(math.sqrt(number))+1):
		if (number%divisor == 0):
			properDivisors.append(divisor)
			if( divisor != number/divisor):
				properDivisors.append(number/divisor)
	return properDivisors


		


def findNonAbundantSums():
	nonAbundantNumbers = []
	abundantNumberSumList = set()
	abundantNumbersList = findAllAbundantNumbers() # first find all abundant numbers under 28124.
	print "Total number  of Abundant Numbers: ",len(abundantNumbersList)

	for j in range(0,len(abundantNumbersList)): # find all numbers that can  expressed as a sum of 2 abundant numbers (under 28124)
		for k in range(j,len(abundantNumbersList)):
			total = abundantNumbersList[j] + abundantNumbersList[k]
			if (total < 28124 ):
				abundantNumberSumList.add(total)
	print "Count of numbers that can be expressed as sum of 2 abundant numbers: ",len(abundantNumberSumList)			

	for m in range(1,28124): # Get all numbers under 28124 that cannot be expressed as a sum of 2 abundant numbers. 
		if (m not in abundantNumberSumList):
			nonAbundantNumbers.append(m)
	return sum(nonAbundantNumbers)		





def main():
	start_time = time.time()
	print "Calling function........"
	requiredSum = findNonAbundantSums()
	print "sum of all the positive integers which cannot be written as the sum of two abundant numbers: ",requiredSum
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	

# Answer: 4179871
# Problem solved in 6.9716861248 seconds	