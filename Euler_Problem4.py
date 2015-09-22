# Largest Palindrome Product:
# Problem Source: https://projecteuler.net/problem=4
# Approach: 1. Find the product of all two 3 digit numbers and store it in a list.
# 2. Start with the largest product in the list.  check if the product is a palindrome. If it is, that number is the desired result. 

import time

# This methdod returns the largest palindrome which is a product of two 3-digit numbers. 
def getProduct():	
	productlist = []
	for i in range(100,1000):
		for j in range(100,1000):
			product = i*j
			productlist.append(product) # list of all products made from two 3-digit numbers.
	productlist.sort(reverse=True)		# sort the product list in descending order. 
	for prod in productlist: # starting from the largest product in the list, check if it is a palindrome.
			if(checkPalindrome(prod)):
				return prod
	

# This method checks whether the given number is a palindrome. 
# To check for palindrome, reverse the given number. If the number and its reverse are identical, then the given number is a palindrome. 
def checkPalindrome(number):
	# The number must be converted to a string so that it can be treated as a list and reversed easily. 
	number = str(number)
	reverse = ''
	for i in xrange(len(number)-1,-1,-1):
		reverse = reverse + number[i]
	if (number == reverse):
		return True
	else:
		return False		


def main():
	start_time = time.time()
	largestPalindrome = getProduct()
	print "The largest palindrome made from the product of two 3-digit numbers is: ", largestPalindrome
	print"Problem solved in %s seconds " % (time.time()-start_time)

if __name__ == "__main__":
	main()