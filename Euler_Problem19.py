# Counting Sundays
# Problem Source = https://projecteuler.net/problem=19
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time

# global variables 
daysInAWeek = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
monthsInAYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
MonthsWith31Days = ['January','March','May','July','August','October','December']
MonthsWith30Days = ['April','June','September','November']
LeapYearsInTwentiethCentury = []

# This method populates a list with all leap years occurring in the 20th century.
def getAllLeapYears(): # A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
	for year in range(1900,2001):
		if (year%100 == 0):
			if (year % 400 == 0):
				LeapYearsInTwentiethCentury.append(year)
			else:
				pass
		elif(year % 4 == 0):
			LeapYearsInTwentiethCentury.append(year)	
	return

# Retuns the day that occurs after a specific number of days(jumps) from a given day of the week.
def getDayOfTheWeek(day,jumps):	
	index_of_the_day = daysInAWeek.index(day)
	resulting_day_of_the_week = index_of_the_day + jumps
	if (resulting_day_of_the_week) < 7:
		return daysInAWeek[resulting_day_of_the_week]
	else:
		return daysInAWeek[resulting_day_of_the_week%7]



def countingSundays():
	# first get the first days of all months for all years and store it in a dictionary
	yearMonthFirstDay = {}
	getAllLeapYears()
	current_starting_day = 'Tuesday'	 # 1st Jan 1901 was a Tuesday.
	for year in range(1901,2001):
		for month in monthsInAYear:
			yearMonthFirstDay[ str(year)+"_"+month ] = current_starting_day
			if month in MonthsWith31Days:
				next_month_starting_day = 	getDayOfTheWeek(current_starting_day,3)	
			elif month in MonthsWith30Days:
				next_month_starting_day = 	getDayOfTheWeek(current_starting_day,2)
			elif(year in LeapYearsInTwentiethCentury): # month is february and year is leap
				next_month_starting_day = getDayOfTheWeek(current_starting_day,1)
			else: # month is february, but year is not leap.
				next_month_starting_day = current_starting_day	
			current_starting_day = 	next_month_starting_day	

	# count number of sundays from the dictionary
	listOfFirstDays = yearMonthFirstDay.values()
	count = 0
	for day in listOfFirstDays:
		if  day == 'Sunday':
			count += 1	
	return	count	



def main():

	start_time = time.time()	
	print "Number of sundays fell on the first of the month during the twentieth century:", countingSundays()
	print"Problem solved in %s seconds " % (time.time()-start_time)




if __name__ == "__main__":
	main()

# Answer: 171