# Self Powers
# Problem 48: https://projecteuler.net/problem=48
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

# Approach: 1. We need to find only the last 10 ten digits of the sum of the above series. We know that, if we calculate (a mod 10), we get the units digit of the number a.
# For e.g. 23 mod 10 = 3. If we want the last 2 digits of a number, we do (a mod 100). So, we want the last 10 digits of a number, we calculate (a mod 10^10).
# 2. We will use a useful property related to modular arithmetic to compute the last 10 digits of the sum of the above series. 
# a) (a+b) mod c == [(a mod c) + (b mod c)] mod c. 
# So, if we compute  (1^1 mod 10^10), (2^2 mod 10^10), ....... we can add the result, compute (result mod 10^10), to get the desired answer. 
# 3. Also, if a^a < 10^10, then a^a mod 10^10 == a^a. So, no need to compute modulo for self powers that are less than 10^10.


import math
import time



def findSelfPowers():
	n = 10**10 # since we want the last 10 digits of the sum of self powers.
	sumOfSelfPowers = 0
	for i in range(1,1001):
		selfpower = i ** i
		if ( selfpower < n): # if self power is less than n, then selfPower mod n == selfpower
			sumOfSelfPowers = sumOfSelfPowers + selfpower
		else:
			sumOfSelfPowers = sumOfSelfPowers + (selfpower % n) 	
	return (sumOfSelfPowers % n)	


def main():
	start_time = time.time()
	print "The last ten digits of the series is : ", findSelfPowers()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer:  	9110846700
