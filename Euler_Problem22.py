# Name scores
# Problem Source = https://projecteuler.net/problem=22
# What is the total of all the name scores in the file?
# Approach:
# 1. Read all the names from the text file in to a list.
# 2. Sort the list of names alphabetically.
# 3. For each name, compute its alphabetical value. 
# 4. Multiply each name's alphabetical value with its position in the list to get its name score.
# 5. Sum all name scores to obtain result. 



import time
import math
import Common




def readTextFile():
	f = open('p022_names.txt','r') # create a file object
	content = f.read() # read all the contents of a file
	words = content.split(',') # split the contents of file by comma.
	return words


def computeTotalNameScores():
	list_of_names = readTextFile()  # read all the names from the text file in to a list.
	list_of_names.sort() # sort all names in the list alphabetically
	sum_of_name_scores = 0
	for name in list_of_names:
		word_value = Common.computeAlphabeticalValue(name) # compute alphabetical value of the name
		sum_of_name_scores = sum_of_name_scores + (list_of_names.index(name)+1)*word_value #Multiply each name's alphabetical value with its position in the list to get its name score.
	return sum_of_name_scores 		


def main():

	start_time = time.time()	
	print "The total of all the name scores in the file is: ",computeTotalNameScores()
	print"Problem solved in %s seconds " % (time.time()-start_time)



if __name__ == "__main__":
	main()

# Answer: 871198282

