# Greatest product of 5 consecutive digits in the 1000 digit number
# Problem Source = https://projecteuler.net/problem=8
# Approach: 1. First read the thousand digit number and convert it to a list containing 1000 elements (i.e. each element corresponds to a digit).
# 2. In the list, take 13 digits sequentially at a time, compute the product and store the product in the list.
# 3. Repeat the process until you run out of digits.
# 4. Get the highest product from the product list. This is our desired result. 

import time

# This methdd computes the product of every 13 consecutive elements in a list and returns the product that has the highest value.
def maxProduct(numberList):
	productList = []
	for i in range(0,len(numberList)):
		prod = 1
		beg = i
		end = i+13
		if (end <= len(numberList)-1):
			for j in range(beg,end):
				prod = prod * numberList[j]
		print beg, end, prod	
		productList.append(prod)
	maxProduct = max(productList)
	return maxProduct
				
# this method converts a number to a list of digits.
def convertNumberToListOfIntegers(inputNumber):
	strNum = str(inputNumber) # first convert number to string format.
	numList = []
	for digit in strNum: # then convert each element in the string in to an integer and append it to a list.
		numList.append(int(digit))
	return numList



def main():

	start_time = time.time()

	# Read each line (containing 50 digits) in to a separate variable.
	a = 73167176531330624919225119674426574742355349194934
	b = 96983520312774506326239578318016984801869478851843
	c = 85861560789112949495459501737958331952853208805511
	d = 12540698747158523863050715693290963295227443043557
	e = 66896648950445244523161731856403098711121722383113
	f = 62229893423380308135336276614282806444486645238749
	g = 30358907296290491560440772390713810515859307960866
	h = 70172427121883998797908792274921901699720888093776
	i = 65727333001053367881220235421809751254540594752243
	j = 52584907711670556013604839586446706324415722155397
	k = 53697817977846174064955149290862569321978468622482
	l = 83972241375657056057490261407972968652414535100474
	m = 82166370484403199890008895243450658541227588666881
	n = 16427171479924442928230863465674813919123162824586
	o = 17866458359124566529476545682848912883142607690042
	p = 242190226710556263211111093705442175069416589604080
	q = 7198403850962455444362981230987879927244284909188
	r = 845801561660979191338754992005240636899125607176060
	s = 5886116467109405077541002256983155200055935729725
	t = 71636269561882670428252483600823257530420752963450
	
	# convert each line of digits in to a list of digits. At the end, You will have one list containing 1000 digits. 
	listOfNumbers = [] # this list will store 1000 digits.
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(a)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(b)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(c)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(d)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(e)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(f)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(g)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(h)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(i)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(j)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(k)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(l)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(m)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(n)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(o)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(p)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(q)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(r)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(s)
	listOfNumbers = listOfNumbers + convertNumberToListOfIntegers(t)
	
	print listOfNumbers
	greatestProduct = maxProduct(listOfNumbers)
	print "The greatest product of the thirteen adjacent digits in the 1000-digit number is: ",greatestProduct
	print"Problem solved in %s seconds " % (time.time()-start_time)




if __name__ == "__main__":
	main()

# Answer: 23514624000