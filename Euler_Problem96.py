def cross(A,B):
	"Cross product of elements in A and B."
	return [a+b for a in A for b in B]


def test():
	"A set of unit test cases."
	assert len(squares) == 81
	assert len(unitlist) == 27
	assert all(len(units[s]) == 3 for s in squares)
	assert all(len(peers[s]) == 20 for s in squares)



def main():
	digits = '123456789'
	rows = 'ABCDEFGHI'
	cols = digits
	squares = cross(rows,cols)
	#print "squares: ",squares
	unitlist = ( [cross(rows,c) for c in cols] + 
				 [cross(r,cols) for r in rows] + 
				 [cross(rs,cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')] 	
				)
	#print unitlist
	units = dict((s,[u for u in unitlist if s in u]) for s in squares)
	print "Units: ",units
	peers = dict((s,set(sum(units[s],[]))-set([s])) for s in squares)
	#print "peers: ",peers








if __name__ == "__main__":
	main()	


