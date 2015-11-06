# Digit cancelling fractions
# Problem 33: https://projecteuler.net/problem=33
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
# Approach: Used Brute Force. See inline comments


import math
import time
import Common

common = Common.Common()


		
def findDigitCancellingFractions():
	digit_cancelling_fractions = []

	for numerator in range(10,100): # since we are interested only in fractions having 2 digits in numerator and denominator.
		for denominator in range(10,100):
			# if value of fraction > 1 or if the units place of numerator or denominator has a 0, skip and go to next number.
			if (   (numerator/denominator >= 1) or (common.getDigits(numerator)[1] == 0) or (common.getDigits(denominator)[1] == 0)):
				pass
			else:
				if (common.getDigits(numerator)[1] == common.getDigits(denominator)[0]):	# Units digit of numerator equals the tens digit of denominator

					# After digit cancelling, if value of incorrect fraction equals value of correct fraction, we have a winner.  
					if (float(common.getDigits(numerator)[0]) / float(common.getDigits(denominator)[1]) == float(numerator)/float(denominator)):
						digit_cancelling_fractions.append((numerator,denominator))


	# find the product of all 4 digit cancelling fractions
	product_numerator = 1
	product_denominator = 1
	# calculate the product of all numerators and denominators separately.
	for fract in digit_cancelling_fractions:
		product_numerator = product_numerator*fract[0] 
		product_denominator = product_denominator*fract[1]
	
	# reduce the fraction to its lowest common term
	reducedform = common.reduceFractionToLowestCommonTerms((product_numerator,product_denominator)) 			
	return	reducedform		


	
def main():
	start_time = time.time()
	print "The value of the denominator is: ", findDigitCancellingFractions()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer: 100
