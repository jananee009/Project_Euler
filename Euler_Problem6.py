# Sum Square Difference


def sumSquareDifference(n):
	sumofSquares = 0
	squareofsum = 0
	
	for i in range(1,n+1):
		sumofSquares = sumofSquares+i*i
		
	sumOfFirst100Numebrs = 	n*(n+1)/2
	squareofsum = sumOfFirst100Numebrs * sumOfFirst100Numebrs
	
	diff = squareofsum - sumofSquares
	
	return diff




def main():
	difference = sumSquareDifference(100)
	print difference
	


if __name__ == "__main__":
	main()