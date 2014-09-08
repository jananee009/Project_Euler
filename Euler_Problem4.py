# Largest Palindrome Product:

def getProduct():
	palindromelist = []
	for i in xrange(999,99,-1):
		for j in xrange(999, 99, -1):
			product = i*j
			if(checkPalindrome(product)):
				print i,j,product
				palindromelist.append(product)
	biggestPalindrome = max(palindromelist)			
	return biggestPalindrome


def checkPalindrome(number):
	number = str(number)
	reverse = ''
	for i in xrange(len(number)-1,-1,-1):
		reverse = reverse + number[i]
	if (number == reverse):
		return True
	else:
		return False		


def main():
	largestPalindrome = getProduct()
	print largestPalindrome
	

if __name__ == "__main__":
	main()