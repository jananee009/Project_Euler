# Pythagorean Triplet
# Problem Source = https://projecteuler.net/problem=39
# For which value of p <=1000, is the number of solutions maximised?
# Approach: See comments inline


import time

	
def integerRightTrianglesBruteForce():
	perimeter_sides = {}
	# since  a+b+c <= 1000; it follows that a<b<c<1000.
	for a in range(1,1000/3): #   the maximum value of a cannot be more than 1/3rd of 1000.
		for b in range(a,1000/2): #At any point, b will be either equal to or greater than the value of a.
			for c in range(b,1000/2):
				if (a+b+c <= 1000):
					if (  a*a + b*b == c*c ): # check for the condition
						if (a+b+c) not in perimeter_sides:
							perimeter_sides[a+b+c] = [[a,b,c]]
						else:
							perimeter_sides[a+b+c].append([a,b,c])	
	

	keys = 	perimeter_sides.keys()
	max_sol = 0
	max_sol_perimeter = 0
	for key in keys:
		if (len(perimeter_sides[key]) > max_sol):
			max_sol = 	len(perimeter_sides[key])
			max_sol_perimeter = key	
	return max_sol_perimeter				
				


def main():
	start_time = time.time()
	print "The value  of p, for which the number of solutions is maximised: ",integerRightTrianglesBruteForce()
	print"Problem solved in %s seconds " % (time.time()-start_time)
	




if __name__ == "__main__":
	main()

# Answer: 840	