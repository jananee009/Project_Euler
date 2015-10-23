# Triangular, Pentagonal, Hexagonal
# Problem Source = https://projecteuler.net/problem=45
# T285 = P165 = H143 = 40755
# Find the next triangle number that is also pentagonal and hexagonal.
# Approach:
# 1. We know that T285 = 40755.
# 2. Compute the next triangular number t.
# 3. Equate t = p*(3*p-1)/2. Solve the quadratic equation p. if p is a whole number go to step 4 else go to step 2.
# 4. Equate t = h*(2*h-1). Solve the quadratic equation h. if n is a whole number go to step 5 else go to step 2.
# 5. t is the required answer. 



import time
import math


# returns the root of the quadratic equation.
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



def findNextTriangularPentagonalHexagonal():
	n = 286  # start from n = 286, as per info given in the problem.
	while(True):
		t = n*(n+1)/2 # compute the triangular number

		#for pentagonal number, equate t =  p*(3*p-1)/2 and solve for p.
		# Equation can be rewritten as 3*p*p-p-2*t = 0. So, a = 3, b = -1, c=-2*t
		if ( solveQuadraticEquation(3,-1,-2*t) > 0):
			# for hexagonal number equate t = h*(2*h-1) and solve for h.
			# Equation can be rewritten as 2*h*h-h-t = 0. So, a = 2, b = -1, c=-t
			if (solveQuadraticEquation(2,-1,-t) > 0):
				return t
		n = n+1		


def main():

	start_time = time.time()	
	print "the next triangle number that is also pentagonal and hexagonal is: ", findNextTriangularPentagonalHexagonal()
	print"Problem solved in %s seconds " % (time.time()-start_time)



if __name__ == "__main__":
	main()

# Answer: 1533776805