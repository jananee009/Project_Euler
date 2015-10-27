

import math
import string

class Common:
	def __init__(self):
		pass

	# computes the alphabetical value of the given word.
	def computeAlphabeticalValue(self, given_word):	
		alphabets = list(string.ascii_uppercase)
		given_word = given_word[1:-1]
		value = 0
		for char in given_word:
			value = value + (alphabets.index(char) + 1)
		return value
				
	
	# Takes a number is as input and returns a list containing the digits of the number. 
	def getDigits(self,num):	
		digits = []	
		if num > 9: # if num is atleast a 2 digit number
			num = str(num)
			for char in num:
				digits.append(int(char))				
		else:
			digits.append(num) # if num is a single digit number
		return digits
			
	

	# Returns True if the given input is a palindrome.	
	def isPalindrome(self, input):
		input = str(input)
		if (input == input[::-1]):
			return True
		else:
			return False	
			


	# converts a decimal number to binary number and returns the binary number
	def convertDecimalToBinary(self,dec_num):	
		bin_num = ""
		dividend = dec_num
		while (dividend > 1):
			bin_num = bin_num + str(dividend % 2)
			dividend = dividend / 2
		if dividend == 1:
			bin_num = bin_num + str(dividend)
		bin_num = int(bin_num[::-1])
		return	bin_num			
					


	# checks if a given number is prime or non prime.
	def isPrime(self,num):
		sqrtNum = int(math.sqrt(num))
		for i in range(2,sqrtNum+1):
			if num % i == 0:
				return False
		return True		
	
	







