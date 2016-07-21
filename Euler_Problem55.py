# Lychrel Numbers
# Problem 55: https://projecteuler.net/problem=55
# Approach: Start with number 11 and go all the way up to 9999.
# 1. Take a number. Reverse it. Add number and its reverse and check if the sum is a palindrome. 
# 2. Keep repeating step 1 for 50 iterations or till you find a sum that is  a palindrome (whichever is earlier)
# 3. If you get a palindrome, go  to step 1 and process next number. If not, add the number to list of lychrel numbers and go step 1 to process next number. 


import math
import time
import Common


# returns True if a given number is Lychrel else returns False
def isLychrel(number):
	iterations = 1
	while (iterations <= 50 ): # for 50 iterations or less
		reversed_number = ""
		# Reverse the given number
		for digit in reversed(Common.getDigits(number)): 
			reversed_number = reversed_number+str(digit)

		# sum number and its reverse 	
		number_added_to_reverse = number+int(reversed_number)

		#  if sum is a palindrome, tell that the given number is not lychrel by returning False.
		if Common.isPalindrome(str(number_added_to_reverse)):
			return False
		iterations +=1 
		number = number_added_to_reverse
	return True		

		


def findLychrelNumbers():
	LychrelNumbers = [ x for x in range(10,10000) if isLychrel(x)]
	return len(LychrelNumbers)



	
def main():
	start_time = time.time() 
	print "Number of Lychrel numbers below ten-thousand are: ", findLychrelNumbers()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 249	
