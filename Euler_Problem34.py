# digit Factorials
# Problem 34: https://projecteuler.net/problem=34
# Approach: Source: https://en.wikipedia.org/wiki/Factorion
# The most important point in this problem is to determine the upper limit. i.e. when to stop checking for factorial digit sums. 
# We know that for 9,999,999: 9!*7 = 2,540,160 and for 99,999,999: 9!*8 = 2,903,040, which is a 7 digit number. Hence we need to check only until 2,540,160.
# Going further, we know that 9!*6 = 2,177,280 and the only 7 digit number not larger than 2,540,160 containing six 9s is 1,999,9999, which is not a factorion by inspection. 
# The next highest sum would be given by 1,999,998, yielding a third upper bound of 1,854,721. 
# The fourth upper bound can be given by 1,999,997 which is 1,819,441.


import math
import time
import Common

common = Common.Common()

# returns the factorial of a number			
def computeFactorial(n):
	if (n==1 or n==0):
		return 1
	return n*computeFactorial(n-1)	


def findFactorialDigitSum(List_Of_Factorials):
	result = []
	for number in range(10,1819441):
		sum_digit_factorials = sum([List_Of_Factorials[x] for x in common.getDigits(number)]) # calculate the sum of factorial of all digits of the number
		if (number == sum_digit_factorials):
			result.append(number)
	return	sum(result)


	
def main():
	start_time = time.time()
	ListOfFactorialValues = [ computeFactorial(i) for i in range(10)] 	
	print "The sum of all numbers which are equal to the sum of the factorial of their digits (excluding 1 and 2) are: ", findFactorialDigitSum(ListOfFactorialValues)
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 40730	
