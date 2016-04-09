# Problem 14: Longest Collatz sequence
# Source: https://projecteuler.net/problem=14
# Which starting number, under one million, produces the longest chain?
# Approach: 1. Starting from 13 and going up to 1000000, compute the collatz sequence for each number. 
# 2. store the number as key and the length of the collatz sequence of that number as value in a dictionary.
# 3. Once the sequence has been computed for all numbers, find the key that has the maximum length of collatz sequence.


import time

def getNumWithLongestCollatzSequence():	 
	dict_sequenceLength = {} # the number and the length of its collatz sequence will be stored in a dictionary as key,value pair.
	for n in range(13,1000000):
		temp = n
		length = 0		
		oneCollatzSequence = [] 
		oneCollatzSequence.append(temp)
		while(n != 1):			
			if( n%2 == 0): # if n is even
				n = n/2
			else: # n is odd
				n = 3*n + 1
								
			if (n in dict_sequenceLength): # if we encounter a number, for which we computed the collatz sequence before, 
				length = dict_sequenceLength[n] # then just look up that number in the dictionary keys and get the corresponding value to get the length of the sequence.
				break						
			else:	
				oneCollatzSequence.append(n)	

		dict_sequenceLength[temp] = len(oneCollatzSequence) + length
		
	# get the number with the has the maximum length of collatz sequence 
	v = list(dict_sequenceLength.values())
	k = list(dict_sequenceLength.keys())
	print "Number with the largest collatz sequence is: ", k[v.index(max(v))]
	return
		




def main():
	start_time = time.time()
	getNumWithLongestCollatzSequence()
	print "Solution found in: ", time.time()-start_time, "seonds."


if __name__ == "__main__":
	main()
	
# Answer: 837799	
	
	
		
		
		
		
	