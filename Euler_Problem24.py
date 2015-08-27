# Question: Lexicographic permutations
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Approach: There are 10 digits. Total number of permutations possible with 10 digits is 10! = 3,628,800. 
# If we fix the first digit in each of the permutations generated, then we know that there will be equal number of permutations for each first digit. 
# For e.g. the number of permutations starting with 0  = 3,628,800/10 = 362,880. 
# If we arrange all the permutations in ascending order, the first 362,880 permutations will begin with 0. The next 362,880 will begin with 1 and so on. 
# From this pattern, we can see that the millionth lexicographic permutation will begin with 2. 
# The number we want will be [1000000-(2*362880)] = 274240th number in the list containing all permutations starting with 2.


import itertools
import time


def permutations():
	listOfPermutations = []
	input = [0,1,3,4,5,6,7,8,9]
	output = itertools.permutations(input,None) # generate all permutations
	output = list(output) # get a list of tuples.
	for perm in output:
		#print perm
		perm = list(perm) # convert tuple to list
		temp = [str(i) for i in perm] #convert each item (number) in list to string
		permStr = '2'+("".join(temp)) #concatenate each string element in list to form one string
		listOfPermutations.append(permStr) # add number to list
	print listOfPermutations[274240]
	return

		
	
def main():
	start_time = time.time()
	print "Calling function........"
	permutations()
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	
# Solution: The millionth term is 2783915460.
	
	
	
		
		
		
		
	