# Question: What is the first term in the Fibonacci sequence to contain 1000 digits?




def fibonacciNumbers():
	a = 1
	b = 1
	c = 0
	count = 2
	while(len(str(c)) < 1000 ):
		count = count + 1
		c = a+b
		temp = b
		a = b
		b = c
	print "count is: ", count
	return
		

		
	
def main():
	fibonacciNumbers()
		
	

if __name__ == "__main__":
	main()	
	
# Solution: The first term in the Fibonacci sequence to contain 1000 digits is 4782.
	
	
	
		
		
		
		
	