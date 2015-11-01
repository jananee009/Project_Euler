# pandigital multiples
# Problem 38: https://projecteuler.net/problem=38
# Approach: 1. We want to  find the largest possible 9 digit pandigital number which is a product of an integer (say x) and (1,2,3,.....n).
# If we find x, we can easily find the pandigital product i.e. the solution to our problem.
# 2. We know that The largest 9 digit pandigital number is 987654321. We can treat this number as the upper bound for our solution. 
# 3. In the problem, we have been given an example how 918273645 is a pandigital poduct formed by multiplying 9 with (1,2,3,4,5).
# 4. So, we know that the solution we are looking for will be atleast 918273645 or greater. Therefore, 918273645 < = solution < = 987654321.
# 5. We can also conclude that x, whether it is a 2-digit, 3-digit or 4-digit or higher number, must begin with 9 because our solution begins with 9.
# 6. Also, x cannot be a 3 digit number because whenever a 3 digit number starting with 9 is multiplied with (2,3,....), we get a 4 digit number. 
# Check the smallest 3 digit number starting with 9. i.e. 901 * 1 = 901; 901 * 2 = 1802; 901*3=2703. On concatenating, we get 90118022703 which is a 11 digit number. 
# So, we can rule out all 3 digit numbers. 
# 7. By similar reasoning, x cannot be a 5 digit number or higher. 
# 8. So, x can be a 2-digit or 4 -digit number starting with 9. So, we will compute products using x lying in range 91 to 98 (both inclusive). 
# 9. And for 4 digit numbers, x's range will begin from 9012 instead of 9001. This is because all numbers from 9001 to 9010 have 2 zeroes and our solution cannot contain any zeroes.
# Also, x's range will end at 9876. All numbers above 9876 will have a repetition of digits and our solution cannot have any digit occur more than once in it.


import math
import time
import Common




def ceatePotentialPandigitalProducts(range_of_numbers, result):	
	common = Common.Common()
	for integer in range_of_numbers:
		prod = 1
		x = ""	
		for n in range(1,10):
			prod = integer * n 
			x = x + str(prod)
			if (len(x) >= 9):
				if ( int(x) < 987654321 and int(x) > result and common.isPandigital(int(x))):
					result = int(x)	
					a = integer
					b = n		
	return result	

			
def findLargestPandigitalProduct():
	result1 = ceatePotentialPandigitalProducts(list(range(91,99)), 918273645) 
	result2 = ceatePotentialPandigitalProducts(list(range(9012,9877)), result1)
	return result2

	
def main():
	start_time = time.time()
	print "The largest 1 to 9 pandigital 9-digit number is : ", findLargestPandigitalProduct()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 932718654	
