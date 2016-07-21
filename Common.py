

import math
import string
import collections



# computes the alphabetical value of the given word.
def computeAlphabeticalValue(given_word):	
	alphabets = list(string.ascii_uppercase)
	given_word = given_word[1:-1]
	value = 0
	for char in given_word:
		value = value + (alphabets.index(char) + 1)
	return value

		
# Takes a number is as input and returns a list containing the digits of the number. 
def getDigits(num):	
	digits = []	
	if num > 9: # if num is atleast a 2 digit number
		num = str(num)
		for char in num:
			digits.append(int(char))				
	else:
		digits.append(num) # if num is a single digit number
	return digits				
				
		

# Returns True if the given input is a palindrome.	
def isPalindrome(input):
	input = str(input)
	if (input == input[::-1]):
		return True
	else:
		return False	
		


# converts a decimal number to binary number and returns the binary number
def convertDecimalToBinary(dec_num):	
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
def isPrime(num):
	sqrtNum = int(math.sqrt(num))
	for i in range(2,sqrtNum+1):
		if num % i == 0:
			return False
	return True		


# A n-digit number is called pandigital if it has all numbers from 1 to n occurring in it exactly once. For e.g., 34521.
def isPandigital(number):
	digits_list = getDigits(number) # get all the digits of the number
	if len(digits_list) == len(set(digits_list)): # if given number has unique digits
		for digit in range(1,len(digits_list)+1): 
			if (not digit in digits_list): # check if n digit number has all digits from 1 to n in it.
				return False
	else:
		return False
	return True		


# returns True if the 2 input numbers are coprime. i.e. the only positive iteger that divides both numbers is 1.
def isCoprime(number1, number2):
	if number1 == number2:
		return False
	number1factors = [i  for i in range(2,number1+1) if number1%i == 0] # find factors of both numbers
	number2factors = [i  for i in range(2,number2+1) if number2%i == 0]		
	if (set(number1factors).intersection(number2factors)): # if both lists have common factors, 
		return False
	else:
		return True	


# accepts a fraction in tuple form (numerator,denominator) and returns a reduced form of the fraction.		
def reduceFractionToLowestCommonTerms(fraction):
	numerator, denominator = fraction # tuple unpacking
	if (numerator <= denominator): # if value of fraction <= 1
		if ((denominator % numerator) == 0):
			lowestCommonTerms = (1,denominator/numerator)
		else:
			while(not isCoprime(numerator,denominator)):
				for i in range(2,(numerator/2)+1):
					if (numerator % i == denominator % i == 0):
						numerator = numerator / i
						denominator = denominator / i
			lowestCommonTerms = (numerator,denominator)
	elif (numerator > denominator): # if value of fraction > 1.
		if ((numerator % denominator) == 0):
			lowestCommonTerms = (numerator/denominator,1)
		else:
			while(not isCoprime(numerator,denominator)):
				for i in range(2,(denominator/2)+1):
					if (numerator % i == denominator % i == 0):
						numerator = numerator / i
						denominator = denominator / i
			lowestCommonTerms = (numerator,denominator)
	return 	lowestCommonTerms	


# returns a list of prime factors of a given number	
def findPrimeFactors(number):		
	list_of_prime_factors = []
	i = 2
	while (number > 1):
		if (number % i == 0):
			list_of_prime_factors.append(i)
			number = number / i
		else:
			i += 1
	return list_of_prime_factors		


# returns the product of numbers in a list
def computeProductOfAList(list_of_numbers):
	prod = 1
	for number in list_of_numbers:
		prod = prod * number
	return prod	


# accepts a number as input and returns -1 if the number CANNOT be expressed purely as power of 2. Otherwise, it returns the power of 2.	
def expressAsPowerOf2(number):
	power = 0
	while (number > 1):
		if (number % 2 == 0):
			power += 1
			number = number / 2
		else:
			return -1
	return power			

# checks if input values are permutations of each other.	
def checkIfPermuted(value1, value2):
	a = set(str(value1))
	b = set(str(value2))

	if a == b:
		return True
	else:
		return False	

# Accepts values of n and r as input and returns value of nCr. 		
def computeCombinations(n,r):
	numerator = math.factorial(n)	
	denominator = 	math.factorial(r) * math.factorial(n-r)
	return (numerator / denominator)




		


			
	







