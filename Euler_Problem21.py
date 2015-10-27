# Amicable Numbers
# Problem 21: https://projecteuler.net/problem=21
# Approach: Maintain a boolean list of size 10,000 with each value set to True. This list will help us avoid checking amicability of a number more than once.
# 1. For a number (index), if it is below 10,000 get proper divisors and sum them. (d1)
# 2. Get the proper divisors of the sum, and sum them up. (d2)
# 3. If number and d2 are equal, go to step 4, else go to step 6.
# 4. Add the number and d2 to a list of amicable numbers. 
# 5. Set the corresponding values in the boolean list to False
# 6. Find the next highest index in the boolean list that has its value set to True. 
# 7. Go to step 2.


import time

# returns a list of proper divisors for a given number
def findProperDivisors(number):
    divisorArray = []
    for i in range(1, (number/2+1)):
        if (number%i == 0):
            divisorArray.append(i)
    return divisorArray



def findAmicableNumbers(limit):
    amicableNumbers = [] # this list will contain all amicable numbers under 10,000.
    listOfNumbers = [True]*(limit+1) # the boolean value will be set to False whenever a number (i.e.index) is tested for amicability.
    index = 2
    d_index, d_sum = 0,0
    while (index < limit):
        d_index = sum(findProperDivisors(index)) # find proper divisors for the number and sum them 
        if (index != d_index):
            d_sum = sum(findProperDivisors(d_index)) # find proper divisors for the sum and sum them.
            if (index == d_sum): # if both sums are equal
                amicableNumbers.append(index) # add both numbers to  the list
                amicableNumbers.append(d_index)
                listOfNumbers[index] = False
                listOfNumbers[d_index] = False
                   
        # get the next highest index from listOfNumbers that has True value  
        for i in range(index+1,limit+1):
            if (listOfNumbers[i]):
                index = i
                break                       
    return sum(amicableNumbers)                  


def main():
    start_time = time.time()
    print "Calling function........"
    limit = 10000
    print "The sum of all the amicable numbers under 10000 is: ", findAmicableNumbers(limit)
    print "Problem solved in %s seconds " % (time.time()-start_time)



if __name__ == "__main__":
    main()



# Answer: 31626 






