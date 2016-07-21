# Problem 58: Spiral Primes
# Source: https://projecteuler.net/problem=58
# Approach: 1. In the problem, we have already been given a square spiral of  side length 7. 
# 2. We need to add another layer of elements, find the new  elements along the right and left diagonal  and check how many of them are prime.
# 3. If we observe the given square spiral, we can see that:
# a. As we add a layer of elements to the square, the side length of the square increases by 2. The side length is always odd .
# b. The maximum element (also a diagonal element) of the square is always an odd square, which is equal to ( side length * side length ).
# c. We can directly find the new diagonal elements (as each new layer is added) from the last layer's  diagonal elements and side length of the square.
# 					Diagonal elements					Square Side length				Max Element
# Layer 0					1									1							1
# Layer 1				3,5,7,9 								3							9
# Layer 2				13,17,21,25								5							25
# Layer 3				31,37,43,49								7							49

# If we add 2 to the diagonal element of the square with length 1, we get the 1st diagonal element of the next layer. 
# You can get the remaining diagonal elements for this layer by adding 2
# If you add 4 to the last diagonal element of the square with length 3, we get the 1st diagonal element of the next layer. 
# You can get the remaining diagonal elements by adding 4 and so on. 
# So, the next set of diagonal elements (for square with side length 9) are (49+8*1, 49+8*2, 49+8*3, 49+8*4) i.e. (57, 65, 73, 81).
# 4. As we find new diagonal elements, for each diagonal element (except for the last one) , we need to check if the element is prime. 



import time
import Common 


def spiralPrimes():
	

	# as given in the problem:
	diagonal_Elements = [1,3,5,7,9,13,17,21,25,31,37,43,49]
	prime_diagonal_elements = [3,5,7,13,17,31,37,43]

	number_of_diagonal_elements = len(diagonal_Elements)
	number_of_prime_diagonal_elements = len(prime_diagonal_elements)

	ratio = number_of_prime_diagonal_elements / float(number_of_diagonal_elements)

	square_side_length = 7

	while (ratio >= 0.1): # as long as the ratio is greater than or equal to 10%, keep adding new layer of numbers. 
		

		# number of diag elements increase by 4 each time a new layer is added. 
		number_of_diagonal_elements += 4  

		# We need to compute  only the first 3 diagonal elements for each layer added and check if each is a prime. We know that the last element is always an odd perfect square. 
		for i in range(1,4):
			#new_diag_element = (square_side_length**2) + (square_side_length+1)*i
			if Common.isPrime((square_side_length**2) + (square_side_length+1)*i):
				number_of_prime_diagonal_elements += 1


		# The length of the side of the square increases by 2 each time we add a new layer. 
		square_side_length += 2	

		# compute ratio
		ratio = number_of_prime_diagonal_elements / float(number_of_diagonal_elements)

		
	return 	square_side_length



def main():
	start_time = time.time()
	print(spiralPrimes())
	print "Solution found in: ",time.time()-start_time, "seconds."


if __name__ == "__main__":
	main()

# Answer: 26241
	
	
	
	
	
		
		
		
		
	