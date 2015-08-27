# Problem 15: Lattice Paths.If you are allowed to move only Down and Right, how many paths are there in a 20*20 grid  from the top left corner to bottom right corner.
# Approach: Use combinations
# Consider a 2*2 grid (N*N grid). all paths can be described as a series of directions. We can go only Down(D) or Right(R).
# We can describe all the paths as a series of Ds and Rs. So, in a 2*2 grid, all paths are:
# 1.RRDD  2.RDRD   3.RDDR  4.DRRD  5.DRDR  6.DDRR
# All paths have the same size (2N) of which there are N Rs and N Ds.
# If we have 2N empty spaces and if we have to choose N spaces to place Ds (or Rs) then this can be done by  computing (2N choose N).
# So, if N=20, (i.e. for a 20*20 grid), the total number of paths can be given by (40 choose 20).


import math
import time

def getLatticePaths(N):
	numerator = math.factorial(2*N)
	denominator = (math.factorial(N))**2
	paths = numerator / denominator
	return paths
		


def main():
	start_time = time.time()
	print "Calling function........"
	print "Total number of paths in a 20*20 lattice grid: ",getLatticePaths(20)
	print"Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	


# Answer: 137846528820	