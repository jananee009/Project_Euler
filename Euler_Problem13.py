# Problem 13: Large Sum
# Source: https://projecteuler.net/problem=13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


import time


def findLargeSum():
	# Read the one-hundred 50-digit numbers
	text_file = open("problem13.txt",'r')
	lines = text_file.readlines() # Read each line of digits from the text file in to a list. List contains one hundred 50 digit numbers in string format.
	

	sumOfNumbers = 0
	numbers = []
	for line in lines: # Convert each line (50 digit number) in to integer form and add it to a new list of numbers. This new list will hold all the 100 numbers.
		numbers.append(int(line))
	
	#Sum all the one hundred 50-digit numbers
	sumOfNumbers = sum(numbers)
	
	#Find the first 10 digits of the sum 
	sumOfNumbers = str(sumOfNumbers)
	first10digits = "" 
	for i in xrange(10):	
		first10digits = first10digits + sumOfNumbers[i]
	print "The first 10 digits are: ", int(first10digits)
	return
		
		



def main():
	start_time = time.time()
	findLargeSum()
	print "Solution found in: ",time.time()-start_time, "seconds."


if __name__ == "__main__":
	main()

# Answer: 5537376230	
	
	
	
	
		
		
		
		
	