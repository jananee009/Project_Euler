# Reciprocal cycles
# Problem Source: https://projecteuler.net/problem=31
# Approach: 1. We have to find all the different ways using which we can change $2 using any number of coins. We have been given a list of available denominations.
# 2. First, consider each available denomination. Find all ways by which we can  change  each denomination. Store it in a dictionary.
# 3. Use this dictionary to find all possible ways to  change a given dollar amount.


import math
import time
import Common
import collections


common = Common.Common()

list_of_denominatons = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1,2]
#list_of_denominatons = [1,2,5,10,20,50,100,200]




dictionary_of_all_changes_for_all_denominations = {  }


# this function accepts a list, an element and a replacement (list) as in put. 
# returns a list with the element removed and replacement list elements added to the original list.
# for e.g. input: ([0.02,0.02,0.02], 0.02, [0.01,0.01]) Output: [0.02,0.02,0.01,0.01]
def replace(inputList, element_to_be_removed, replacement):
	if element_to_be_removed in inputList:
		inputList.remove(element_to_be_removed)
		inputList.extend(replacement)
	return inputList

# list1 is a list of lists. This method checks if list2 exists in list1.
def checkListAlreadyExists(list1,list2):
	compare = lambda x, y: collections.Counter(x) == collections.Counter(y)	# anonymous function to compare 2 lists for equality
	for eachList in list1:
		if (compare(eachList, list2)):
			return True
	return False		



def make_change(dollar_amount,deno_list): 
	big_list = [] # list of all ways to change a dollar amount using a specific set of denominations
	small_list = [] # one way to change a dollar amount  
	for d in deno_list:
		#print "d is:", d
		q = dollar_amount // d
		r = round(dollar_amount % d,2)
		#r = dollar_amount % d
		small_list = [d] * int(q) 
		if r > 0:
			small_list.append(r) 
		big_list.append(small_list)	
		#print "big list1: ",big_list
		if d == min(list_of_denominatons): 
			continue			
		if d not in dictionary_of_all_changes_for_all_denominations: 
			continue
		change_denoms = dictionary_of_all_changes_for_all_denominations[d]	
		#print "change_denoms: ", change_denoms	
		for c  in change_denoms:
			#print "c: ", c 
			temp = small_list[:]
			new_small_list = replace(temp,d,c)
			#print "new_small_list: ", new_small_list
			if (checkListAlreadyExists(big_list,new_small_list)):
				#print "skipping: ", new_small_list
				continue
			big_list.append(new_small_list)
			#print "big list2: ",big_list
			temp = small_list[:]
			for x in range(2,int(q+1)):
				#print "in for loop", x
				#print "small_list: ", temp
				temp = replace(temp,d,c)
				#print "new_small_list: ", temp
				if (checkListAlreadyExists(big_list,temp)):
					#print "skipping: ", temp
					continue
				temp2 = temp[:]	
				big_list.append(temp2)
				#print "big list3: ",big_list
			#print "big list: ",big_list
	#print "final answer:"
	#for list1 in big_list:
	#	print list1													
	return big_list



def find_all_ways_to_change_all_denominations():

	for d in list_of_denominatons:
		change = make_change(d,[deno for deno in list_of_denominatons if deno <= d ])
		dictionary_of_all_changes_for_all_denominations[d] = change
	for key in 	dictionary_of_all_changes_for_all_denominations:
		print key," : ", len(dictionary_of_all_changes_for_all_denominations[key])
	return



def main():
	start_time = time.time()
	find_all_ways_to_change_all_denominations()
	#make_change(10, [1, 2, 5, 10 ])
	print"Problem solved in %s seconds " % (time.time()-start_time)

	

if __name__ == "__main__":
	main()


# Answer: 	