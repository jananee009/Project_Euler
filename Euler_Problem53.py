# Combinatoric selections
# Problem Source: https://projecteuler.net/problem=53
# Approach: In this problem we need to compute nCr for 23 <= n <= 100 and r<=n such that nCr > 1000000.
# We know that nC1 = n, nCn = 1, nCr = nCn-r, nCn-1 = n. Hence, for any n, range for r will be 2 <= r <= n-2.
# Also, while computing values of nCr for a specific n and r = {1,2,3,....n}, we can see that the value keeps on increasing as r increases up to a certain value of r
# after which the value of nCr starts decreasing. i.e. if for a specific n, if the value of nCr1 exceeds 1000000, it will keep increasting until nCn-r1. 
# After r = n-r1, the value of nCr will start to decrease. This is because of the property : nCr = nCn-r
# So, for a specific n, we compute values of nCr for each value of r where r = {2,3,4,....}. When the value of nCr exceeds 1,000,000, for r = r1, 
# we compute r2 = n-r1. We know that nCr1 = nCr2 and both these values are above 1,000,000 and values of nCr for r1<r<r2 will also be above 1000000. 


import math
import time
import Common




def findCombinatoricSelections():
	ncr_more_than_1m = 0 # keeps track of the required values
	
	

	for n in range(23,101): # as given in the question.
		for r in range(2,n-2):
			comb = Common.computeCombinations(n,r)
			if (comb > 1000000):
				# store the value of r for which nCr exceeds 1,000,000
				r1 = r

				# from the property of factorials,  we know that nCr keeps increasing from nCr1 until nCn-r1. Let r2 = n-r1.
				# Hence the number of values that exceed 1,000,000 is (r2-r1+1).

				r2 = n-r1

				ncr_more_than_1m = ncr_more_than_1m + (r2-r1+1)
				break
	return 	ncr_more_than_1m		




def main():
	start_time = time.time()
	print findCombinatoricSelections()
	print"Problem solved in %s seconds " % (time.time()-start_time)

	

if __name__ == "__main__":
	main()


# Answer: 	4075
