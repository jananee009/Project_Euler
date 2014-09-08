# What is the value of the first triangle number to have over five hundred divisors?
import time
import math

def generateTriangleNumbers():
	number = 3
	counter = 3
	while(not generateDivisors(number)):		
		counter = counter + 1
		number = counter*(counter+1)/2		
	return number		


def generateDivisors(num):	
	if (num==1 or num==3):
		return False
	count = 1
	for i in range(1,int(math.sqrt(num))+1):
		if(num%i==0):
			count = count + 1
	if( (count*2)>500):
		print count*2
		return True
	else:
		return False
										

def main():
	start_time = time.time()
	requiredNumber = generateTriangleNumbers()
	print requiredNumber
	print (time.time() - start_time), "seconds"
	


if __name__ == "__main__":
	main()