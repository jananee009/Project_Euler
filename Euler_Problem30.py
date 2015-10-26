# Digit fifth powers
# Problem 30: Digit Fifth Powers
# Approach: Starting from 2, We need to loop through each number and test if it satisfies the condition. But how do we know where to stop?
# For e.g. the lowerst 4 digit number is 1000 and the highest is 9999. The fifth powers of both these numbers is 1 and 236196. Somewhere in between these 2 numbers,
# we may find a number whose digit fifth powers may add up to the 4 digit number itself.
# Similarly, the highest sum of 5th powers of a 5 digit number is 	295,245. we may find a number whose digit fifth powers may add up to the 5 digit number itself.
# The highest sum of 5th powers of a 6 digit number is 	354,294. we may find a number whose digit fifth powers may add up to the 6 digit number itself.
# With a 7 digit number, the highest value is 413343. i.e. the highest sum of the 5th powers of a 7 digit number only adds up to a 6 digit number. 
# So, we need to loop only from 2 to 354294.


import math
import time
import Common

common = Common.Common()


			
def findDigitFifthPowers():
	DigitfifthPowers = []
	for number in range(2,354295): 
		numberDigits = common.getDigits(number) # find the individual digits of the number
		sumOfFifthpowers = sum([x**5 for x  in numberDigits]) # compute fifth power of each digit of the number and sum them.
		if number == sumOfFifthpowers: # if number equals the sum
			DigitfifthPowers.append(number) # add the number to the list.
	return sum(DigitfifthPowers) # sum all the numbers in the list to get the result.		


	
def main():
	start_time = time.time()
	print "Calling function........"
	print "the sum of all the numbers that can be written as the sum of fifth powers of their digits: ", findDigitFifthPowers()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 443839	
