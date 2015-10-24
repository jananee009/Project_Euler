# Double base palindrome
# Problem Source = https://projecteuler.net/problem=36
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# Approach: Read comments inline

import time
import Common 

common = Common.Common()

def findDoubleBasePalindrome():
	doublebasepalindromes = []
	for d in range(1,1000000): # for each decimal number below 1 million
		if (common.isPalindrome(d)): # check if number is a palindrome
			if(common.isPalindrome(common.convertDecimalToBinary(d))): # convert the decimal number to binary and check if it is a palindrome
				doublebasepalindromes.append(d) # add it to the list
	sum_doublebasepalindromes = sum(doublebasepalindromes)	# sum all double base palindromes.	
	return sum_doublebasepalindromes	



def main():
	start_time = time.time()
	print "The sum of all numbers, less than one million, which are palindromic in base 10 and base 2: ",findDoubleBasePalindrome()
	print"Problem solved in %s seconds " % (time.time()-start_time)
	

if __name__ == "__main__":
	main()

# Answer: 840	