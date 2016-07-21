# Problem 16: Power digit sum
# What is the sum of the digits of the number 2^1000?



def computePowerDigit():
	
	value = 1
	for i in range(1,1001):
		value = value*2
	print "value is: ",value
	
	#compute sum of digits of 2^1000
	value = str(value)
	sum = 0
	
	for j in range(0,len(value)):
		sum = sum+int(value[j])
		
	print "sum is: ",sum
	return
	
def main():
	computePowerDigit()
		
	

if __name__ == "__main__":
	main()	
	
	
# Answer: 1366	
	
		
		
		
		
	