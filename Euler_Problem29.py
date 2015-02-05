# Problem 29: Distinct Powers.
# Approach: Solve the problem using brute force method. This method is surprisingly very fast.
# Use a set to store all the distinct powers, instead of a list. 
# This is because checking whether an element is present in a set is a constant time operation, whereas checking a list is a linear time operation.
# You can also think about other approaches like getting prime factorizing the numbers, etc. But brute force method is very simple and works well for this problem.



import time


def countDistinctPowers():
	limit = 101
	distinctPowers = set()
	for a in range(2,limit):
		for b in range(2,limit):
			c = a**b
			if c in distinctPowers:
				pass
			distinctPowers.add(c)	
	print "Number of distinct powers:  ",len(distinctPowers)
	return		

	
def main():
	start_time = time.time()
	print "Calling function........"
	countDistinctPowers()
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	
	
# Solution:
# Number of distinct primes generated: 9183
	
		
		
		
		
	