# Question: Lexicographic permutations
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Approach: Solved using brute force.


import itertools
import time


def findPermutations():
	listOfPermutations = []
	input = [0,1,2,3,4,5,6,7,8,9]
	output = itertools.permutations(input,None) # generate all permutations. output is a list of tuples. Each tuple is a permutations and it is a list of digits.
	for perm in output:
		temp = ''.join([ str(i) for i in perm]) #convert  a tuple of digits in to a string of digits
		listOfPermutations.append(temp) # add each string to a list.
		if len(listOfPermutations) == 1000000: # exit for loop once we have a million strings.
			break 
	return int(listOfPermutations[-1]) # return the millionth item in the list

		
	
def main():
	start_time = time.time()
	print "Calling function........"
	print "The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is: ", findPermutations()
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	
# Solution: The millionth term is 2783915460.
	
	
	
		
		
		
		
	