# Even Fibonacci numbers
# Problem Source: https://projecteuler.net/problem=2
# Approach: Generate a list of fibonacci numbers up to 4 million. 
# In the list, find all even fibonacci numbers and sum them to get the desired result. 

import math
import time

# get a list of all fibonacci numbers under 4 million 
def generateFibonacciNumbers(max):
	fiboList = []
	fiboList.append(1)
	fiboList.append(1)
	while (fiboList[len(fiboList)-1] < max):
		newElement = fiboList[len(fiboList)-1] + fiboList[len(fiboList)-2]
		fiboList.append(newElement)
	return fiboList
	
# find even fibonacci numbers in the list and return their sum.	
def addEvenNumbersInAList(list):
	sum = 0
	for i in list:
		if (i % 2 == 0):
			sum = sum + i
	return sum
		

def main():
	start_time = time.time()
	print "Calling function........"
	maxLimit = 4000000
	fibonnaciNumbersList = generateFibonacciNumbers(maxLimit)
	sumFiboNumbers = addEvenNumbersInAList(fibonnaciNumbersList)
	print "Sum of even valued terms in fibonacci sequence under 4 million is: ",sumFiboNumbers
	print"Problem solved in %s seconds " % (time.time()-start_time)	
	


if __name__ == '__main__':
	main()

# Answer: 4613732	