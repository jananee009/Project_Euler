# Problem 14: Which starting number, under one million, produces the longest chain?



def getNumWithLongestCollatzSequence():	 
	dict_sequenceLength = {}
	for n in range(13,1000000):
		temp = n
		length = 0		
		oneCollatzSequence = []
		oneCollatzSequence.append(temp)
		while(n != 1):			
			if( n%2 == 0):
				n = n/2
				if (n in dict_sequenceLength):
					length = dict_sequenceLength[n]
					break						
				else:	
					oneCollatzSequence.append(n)
			else:
				n = 3*n + 1
				if (n in dict_sequenceLength):
					length = dict_sequenceLength[n]
					break						
				else:	
					oneCollatzSequence.append(n)						
		dict_sequenceLength[temp] = len(oneCollatzSequence) + length
		
	
	v = list(dict_sequenceLength.values())
	k = list(dict_sequenceLength.keys())
	print "Number with the largest collatz sequence is: ", k[v.index(max(v))]
	return
		







		



def main():
	getNumWithLongestCollatzSequence()


if __name__ == "__main__":
	main()
	
	
	
	
		
		
		
		
	