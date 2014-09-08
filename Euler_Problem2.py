# Even Fibonacci numbers

def generateFibonacciNumbers(max):
	fiboList = []
	fiboList.append(1)
	fiboList.append(1)
	while (fiboList[len(fiboList)-1] < max):
		newElement = fiboList[len(fiboList)-1] + fiboList[len(fiboList)-2]
		fiboList.append(newElement)
	return fiboList
	
def addEvenNumbersInAList(list):
	sum = 0
	for i in list:
		if (i % 2 == 0):
			sum = sum + i
	return sum
		

def main():
	maxLimit = 4000000
	fibonnaciNumbersList = generateFibonacciNumbers(maxLimit)
	sumFiboNumbers = addEvenNumbersInAList(fibonnaciNumbersList)
	print sumFiboNumbers


if __name__ == '__main__':
	main()