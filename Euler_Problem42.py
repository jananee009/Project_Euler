# Coded Triangle Numbers
# Problem Source = https://projecteuler.net/problem=42
# In the attached text file containing English words, how many are triangle words?
# Approach:
# 1. Read all the words from the text file. 
# 2. For each word, compute the word value. 
# 3. Check if word value is a triangle numer: Equate word_value = n*(n+1)/2. Solve the equation for n. 
# 4. If n is a positive integer, increment count of triangular words.
# 5. Go to step 2. Keep repeating this process until there are no more words to process.


import time
import math
import Common


# computes the root of the quadratic equation.
def solveQuadraticEquation(a,b,c):
	discriminant = b*b - 4*a*c
	
	if (discriminant >= 0): # there are real roots
		root1 = (-b + math.sqrt(discriminant))/(2*a)
		
		if ( root1 > 0 and root1 == int(root1)):
			return int(root1)
		else:
			root2 = (-b - math.sqrt(discriminant))/(2*a)
			
			if ( root2 > 0 and root2 == int(root2)):
				return int(root2)
	return -1 # means there are no real roots					

# computes the value of the given word.
def computeWordValue(given_word):	
	given_word = given_word[1:-1]
	value = 0
	for char in given_word:
		value = value + (alphabets.index(char) + 1)
	return value	


def readTextFile():
	f = open('p042_words.txt','r') # create a file object
	content = f.read() # read all the contents of a file
	words = content.split(',') # split the contents of file by comma.
	return words


def findTriangleWordCount():
	# read all the words from the text file in to a list.
	list_of_words = readTextFile()

	list_of_triangular_words = [] # will store all the triangular words.

	for word in list_of_words:
		word_value = Common.computeAlphabeticalValue(word) # compute word value.

		# check if the word value is a triangular number
		# The equation word_value = n*(n+1)/2 can be rewritten as n*n + n - 2*word_value = 0
		# Thus, a = 1, b = 1, c = -2*word_value
		if (solveQuadraticEquation(1,1,-2*word_value) > -1):
			list_of_triangular_words.append(word)

	return len(list_of_triangular_words)		


def main():

	start_time = time.time()	 
	print "In the attached text file containing English words, number of triangle words is: ",findTriangleWordCount()
	print"Problem solved in %s seconds " % (time.time()-start_time)



if __name__ == "__main__":
	main()

# Answer: 162

