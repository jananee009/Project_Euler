# Pandigital Products
# Problem 32: https://projecteuler.net/problem=32
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# Approach:
# 1. We want to find a product  such that multiplicand * multiplier = product and the multiplicand, multiplicant and product taken together form a pandigital number
# of 9 digits. 
# 2. From the example given in the problem itself we know that a 2 digit number multplied with a 3 digit number may yield a product and they may all together form a 
# pandigital number. 
# 3. We need to find in what other ways can we find a pandigital product. Consider the following table.

#										Multiplier	
#							1-digit		2-digit				3-digit				4-digit
#				1-digit		1,2 digits	2,3 digits			3,4 digits			4,5 digits
# Multiplicand	2-digit		2,3 digits	3,4 digits			3,4,5 digits		6 digits
#				3-digit	    3,4 digits	3,4,5 digits    	5 or more digits	6 or more digits
#				4-digit		4,5 digits	5 or more digits	6 or more digits	8 or more digits

# From the above confusion matrix, we can see that only the following 2 types of multiplicands and multipliers suit our requirement:
# Multiplicand      Multiplier
# 1-digit			4-digit    
# 2-digit			3-digits

# Anything other than the above 2 types results in a multiplicand/multiplier/product identity longer than 9 digits. 	


import math
import time
import Common
import itertools 


def fingPandigitalProdcuts():	
	pandigitalProducts = {0} # we are using a set because we want to avoid adding duplicate pandigital products.

	# 2 digit multiplicands are multiplied with 3-digit multipliers
	for multiplicand in range(12,99):
		for multiplier in range(102, 988):
			product = multiplicand * multiplier # compute product
			multiplicand_nultiplier_product = int(str(multiplicand) + str(multiplier) + str(product)) # form a single identity using the multiplicand, multiplier and product
			if (Common.isPandigital(multiplicand_nultiplier_product)): # check if the identity is pandigital
				pandigitalProducts.add(product) # add product to the set of pandigital products.

	# 1 digit multiplicands are multiplied with 4-digit multipliers			
	for multiplicand in range(1,10):
		for multiplier in range(1002, 9877):
			product = multiplicand * multiplier # compute product
			multiplicand_nultiplier_product = int(str(multiplicand) + str(multiplier) + str(product)) # form a single identity using the multiplicand, multiplier and product
			if (Common.isPandigital(multiplicand_nultiplier_product)): # check if the identity is pandigital
				pandigitalProducts.add(product) # add product to the set of pandigital products.
	 				
	return	sum(pandigitalProducts)	


	
def main():
	start_time = time.time()
	print "The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is:", fingPandigitalProdcuts()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 45228 	
