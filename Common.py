

import math

class Common:
	def __init__(self):
		pass

		
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
	
	







