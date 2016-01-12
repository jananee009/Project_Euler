# Powerful Digit Sum
# Problem 56: https://projecteuler.net/problem=56
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
# Approach: 1. We know that both a and b must be less than 100. 
# We can solve this problem using brute force where we calculate every value of a^b, for a<100 and b<100 and compute thte digital sum. 
# 
# Let us find another non brute force method to solve the problem
# a) If we can reduce the range of the base and the range of the power to be computed, we can cut down the computing time considerably.
# b) Also, it will be useful to know how many digits a^b has without computing the actual value of a^b. 
# This is because the more number of digits a^b has, the higher the chances of its digital sum being large (excluding the powers of 10).
# 
# To find the number of digits in a^b, consider the smallest 4 digit and 5 digit numbers: 1000 and 10,000
# 1000 = 10^3 and 10,000 = 10^4. 1000 has 3 + 1 = 4 digits. 10,000 has 4 + 1 = 5 digits. Hence, all the numbers between 1000 and 10000 will have 4 digits.
# i.e. the number of digits in 1000 and 10,000 is one more than their 10th power.
# So, in general we can write: Number of digits = roundDownToNearestInteger[1 + log10(a^b)] = roundDownToNearestInteger[1 + b*log10(a)].
# Now, consider a number in between 1000 and 10,000. For e.g. 1357. 
# According to the above formula, Number of digits = roundDownToNearestInteger[1 + log10(1357^1)] = roundDownToNearestInteger[1+3.132579847659737] = 4.
# To find the  number of digits in say 73^26: floor[1 + log10(73^26)] =  floor[1+26*log10(73)] = floor(49.44639436313185) = 49
# 
# To find the range of bases and powers we need to consider: we need to find which bases raised to which powers gives numbers with large number of digits. 
# From the info given in the problem, we can ignore powers of 10, since they will always result in a digital sum of 1. 





import math
import time
import Common



			
def findMaximumDigitalSumBruteForce():
	common = Common.Common()
	maxSum = 0
	for a in range(2,100):
		for b in range(2,100):
			value = a**b
			if value < 10:
				continue
			else:
				digitalSum = sum(common.getDigits(value))
				if digitalSum > maxSum:
					maxSum = digitalSum	 	
	return maxSum
		

	
def main():
	start_time = time.time()
	print "The maximum digital sum is : ", findMaximumDigitalSumBruteForce()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		

if __name__ == "__main__":
	main()	
	

# Answer:  	972
