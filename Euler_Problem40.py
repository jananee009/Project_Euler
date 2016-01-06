# Champernowne's constant
# Problem 40: https://projecteuler.net/problem=40
# Approach: We need to find the value of th expression: d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 in the irrational decimal 0.123456789101112131415161718192021... ?
# i.e. We need to find out the 1st, 10th, 100th digit......1000000th digit  in the irrational decimal fraction. 
# The decimal part of the fraction is nothing but 1,2,3,4,....... written consecutively, where d1=1, d2=2,d3=3,........d9=9,d10=1,d11=0, and so on. 
# We need to figure out how far we need to write the series 1,2,3,4,...... to find  d1, d10, d100, d1000, d10000, d100000, d1000000.
# Surely, it is less than 1000000 because we are interested only up to d1000000.
# By observing the series of numbers, we can see that:
# 1...9 corresponds to d1...d9.
# 10...20 corresponds to d10...d31.
# 21...30 corresponds to d32...d51.
# 31...99 corresonponds to d52...d189
# Similarly, the series 100...999 has 900 numbers which contain 2700 digits among them. So, starting from 190 (i.e. d190), the digit count will end at  190 + 2700 - 1 = 2889. (Note: 2889 - 190 + 1 = 2700).
# so, 100...999 corresonponds to d190...d2889.
# BY same logic, The series 1000...9999 has 9000 numbers which contain 9000*4=360000 digits among them. So, starting from 2890 (i.e. d2890), the digit count will end at 2890 + 36000 - 1 = 38889. (Note: 38889 - 2890 + 1 = 36000).
# So, 1000...9999 corresponds to d2890...d38889.
# The series 10000...99999 has 90000 numbers which contains 90000 * 5 = 450,000 digits among them. So, starting from 38890 (i.e. d38890), the digit count will end at 38890 + 450000 - 1 = 488889. (Note: 488889 - 38890 + 1 = 450000 ).
# So, 10000...99999 corresponds to d38890...d488889.
# Now, we want 1000000th digit in the series of numbers. We have covered up to 488889th digit. Thus, We have 1000000 - 488889 - 1= 511110 more digits to cover. 
# Each of these digits belong to 6 digit numbers. So, we need to cover 511110 / 6 = 85185 numbers starting from 100000. 
# So, the series 100000...185185 has 85185 numbers which contains 85185*6 = 511110 digits among them. So, starting from 488890 (i.e. d488890), the digit count will end at 488890 + 511110 - 1 = 999999. (Note: 999999 - 488890 + 1 = 511110).
# So, 100000...185185  corresponds to d488890...d999999.
# Thus, d1000000 will be 1.
# So, we have: 
# d1 = 1.
# d10 = 1
# d100 = ? We can get d100 if we pass 48 digits after d52. These 48 digits belong to 2 digit numbers. i.e. we are looking at 48/2=24 numbers after 31.
# Hence 31 + 24 = 55. Thus d100 = 5.
# d1000 = ? We can get d1000 if we pass 900 digits after d100. These 900 digits belong to 3 digit numbers i.e. we are looking at 900 / 3 = 300 numbers after 100.



import time
import Common




			
		

	
def main():
	start_time = time.time()
	print "The largest n-digit pandigital prime that exists is : ", findLargestPandigitalPrime()
	print "Problem solved in %s seconds " % (time.time()-start_time)
	
		
	

if __name__ == "__main__":
	main()	
	

# Answer:  	
