# Pythagorean Triplet
# Problem Source = https://projecteuler.net/problem=9
# Approach: 1. By Brute Force: See the inline comments in the pythagoreanTripletBruteForce() method to understand the logic.
# 2. By using Euclid's Pythagorean Triplet Generating Formula:
# a) Given any positive integers m and n where m > n > 0, the integers
# a = m*m-n*n
# b =2m*n
# c = m*m + n*n
# Substituting the values of a,b,c in the equation a+b+c = 1000, we get m*(m+n)=500.
# The maximum values of m and n each cannot be more than 500. 


import time

# This method describes an efficient way of solving the problem
def pythagoreanTriplet():
	for m in range(1,500):
		for n in range(1,500):
			if (m*(m+n)==500):
				a = m*m - n*n
				b = 2*m*n
				c = m*m + n*n		
	return a*b*c


# this method solves the problem using bruteforce	
def pythagoreanTripletBruteForce(s):
	# since a,b,c must form a pythagorean triplet and a+b+c = 1000; it follows that a<b<c<1000.
	for a in range(1,s/3): #   the maximum value of a cannot be more than 1/3rd of 1000.
		for b in range(a,s/2): #At any point, b will be either equal to or greater than the value of a.
			c = s-a-b # And since a+b+c = 1000, the value of c will be  computed as 1000-a-b.
			if (  a*a + b*b == c*c ): # check for the condition
					return  a*b*c
				


def main():
	start_time = time.time()
	prod = pythagoreanTripletBruteForce(1000) # the sum of three numbers forming the triplet must be 1000.
	print "Product of Pythagorean triplet whose sum is 1000 is: ",prod
	print"Problem solved in %s seconds " % (time.time()-start_time)
	




if __name__ == "__main__":
	main()