# Problem 13:
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


def readTxtFile():
	text_file = open("problem13.txt",'r')
	lines = text_file.readlines()
	print type(lines)
	sumOfNumbers = 0
	numbers = []
	for line in lines:
		numbers.append(int(line))
	print "size of numbers: ",len(numbers)
	print "first number is: " ,numbers[0] 
	
	#Adding all the 50 100-digit numbers
	sumOfNumbers = sum(numbers)
	
	#Find the first 10 digits of the sum 
	sumOfNumbers = str(sumOfNumbers)
	print "The first 10 digits are: "
	for i in xrange(10):	
		print int(sumOfNumbers[i])
		
		



def main():
	readTxtFile()


if __name__ == "__main__":
	main()
	
	
	
	
		
		
		
		
	