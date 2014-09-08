# Pythagorean Triplet

# This method describes an efficient way of solving the problem
def pythagoreanTriplet():
	for m in range(1,500):
		for n in range(1,500):
			if (m*(m+n)==500):
				a = m*m - n*n
				b = 2*m*n
				c = m*m + n*n		
	return a*b*c
	
def pythagoreanTripletBruteForce():
	for a in range(3,1001):
		for b in range(4,1001):
			for c in range(5,1001):
				if ( (a+b+c == 1000) and (a*a + b*b == c*c) ):
					print "yaay!"
					return  a*b*c
				


def main():
	prod = pythagoreanTriplet()
	print prod
	




if __name__ == "__main__":
	main()