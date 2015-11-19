# Sub-string divisibility
# Problem 41: https://projecteuler.net/problem=43
# Find the sum of all 0 to 9 pandigital numbers with this property.
# Approach: 1. We can use brute force approach in which we generate all possible 10 digit numbers containing 0 to 9. Then, we can apply all the divisibility conditions 
# to each number and find which numbers satisfy all the conditions. 
# 2. The other way is to check the rules and see if we can solve the problem by hand (non programmatically):
# 3. d4d5d6 must be divisible by 5. So, d6 must be 0 or 5.
# 4. d6d7d8 must divisible by 11. So, if d6 is 0, d6d7d8 must be one of numbers such as {011,022,033,.....,099} which is invalid. Hence d6 must be 5.
# If d6 is 5 and d6d7d8 must have all unique digits and be divisible by 11, then it must one of numbers such as {506, 517, 528, 539, 561, 572, 583, 594}
# 5. Since d7d8d9 must be divisible by 13, begin with {06,17,28,39,61,72,83,94} and not contain any 5 or repeat digits, our set of possible numbers for d7d8d9
# becomes {286, 390, 728, 832}.
# 6. Since d8d9d10 must be divisible by 17, begin with {86, 90, 28, 32} and not contain any 5 or repeat digits, our set of possible numbers for d8d9d10 becomes
# {867,289,901}.
# 7. Thus d6d7d8d9d10 = {52867, 53901, 57289}
# 8. Since d5d6d7 must be divisible by 7 and end with {52,53,57}, our set of possible numbers for d5d6d7 becomes {952,357}.
# 9. So, we know that our soultion set has numbers that end with { .....952867 or .....357289}.
# 10. d3d4d5 must be divisible by 3 and d4 must be {0,2,4,6,8}. 
# a) Consider the number ending with .....952867.  
# Here, d4 can be {0,4}.If d5 = 9, d4 = 0 then d3 must be 3. So, we have a possible solution that ends with {..30952867}.
# Since 1 and 4 are the only mumbers left, our required solution subset is {1430952867,4130952867}.
# But if d4 = 4, then we cant have d3d4d5 divisible by 3 by substituting any of the remanining numbers in d3. So, d4 cannot be 4. 
# b) Consider the number ending with ......357289.
# Here d4 can be {0,4,6}. If d5 = 3, d4 = 0, then d3 must be 6. So, we have a possible solution that ends with {..60357289}.
# Since 1 and 4 are the only mumbers left, our required solution subset is {1460357289,4160357289}.
# If d5 = 3, d4 = 6, then d3 must be 0. So, we have a possible solution that ends with {..06357289}.
# Since 1 and 4 are the only mumbers left, our required solution subset is {1406357289,4106357289}.
# If d5 = 3 and d4 = 4, then we cant have d3d4d5 divisible by 3 by substituting any of the remanining numbers in d3. So, d4 cannot be 4.
# Thus our required solution set is {1430952867,4130952867,1460357289,4160357289,1406357289,4106357289}.
# Adding these numbers gives us: 16695334890


# Solved the problem using brute force.

import math
import time
import Common
import itertools 


			
def findPandigitalNumWithSubstringDivisibility():
	all_permutations = [list(perm) for perm in itertools.permutations([0,1,2,3,4,5,6,7,8,9])] # find all 10 digit numbers (actually list of digits) that can be formed.
	PandigitalNumWithSubstringDivisibility = [] # Stores lists of digits that satisfy all the substring divisibility properties.
	for d in all_permutations:		
		if d[0] == 0: # left most digit cannot be 0.
			continue
		elif(d[3] not in [0,2,4,6,8]): #  divisibility by 2
			continue
		elif(d[5] != 5): # divisibility by 5
			continue
		elif(int(''.join(map(str,[d[2],d[3],d[4]]))) % 3 != 0): # divisibility by 3
			continue	
		elif ( int(''.join(map(str,[d[5],d[6],d[7]]))) % 11 != 0 ): # divisibility by 11
			continue
		elif ( int(''.join(map(str,[d[4],d[5],d[6]]))) % 7 != 0 ): # divisibility by 7
			continue
		elif ( int(''.join(map(str,[d[6],d[7],d[8]]))) % 13 != 0 ): # divisibility by 13
			continue
		elif ( int(''.join(map(str,[d[7],d[8],d[9]]))) % 17 != 0 ): # divisibility by 17
			continue
		PandigitalNumWithSubstringDivisibility.append(d)
	solutionSet = [] # stores all the pandigital numbers that satisfy the the substring divisibility properties.
	for num in PandigitalNumWithSubstringDivisibility: # convert each list of digits to a number.
		solutionSet.append(int(''.join(str(i) for i in num))) 
	return sum(solutionSet)	


	
def main():
	start_time = time.time()
	print "the sum of all 0 to 9 pandigital numbers with substring divisibility is: ", findPandigitalNumWithSubstringDivisibility()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
	

if __name__ == "__main__":
	main()	
	

# Answer: 16695334890

