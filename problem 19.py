def daysInMonth(month, year):
	if (month in {9, 11, 6, 4}):
		return 30
	if (month == 2):
		if ( isLeapYear(year) ):
			return 29
		else: 
			return 28
	else:
		return 31

#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
def isLeapYear(year):
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		return True
	else:
		return False

currentYear = 1901
currentMonth = 1
currentDay = 1
currentWeekday = 2
count = 0

while (not (currentDay == 31 and currentYear == 2000 and currentMonth == 12)):
	
	if (currentDay > daysInMonth(currentMonth, currentYear) ):
		currentMonth += 1
		currentDay = 1
	
	if (currentMonth == 13):
		currentYear += 1
		currentMonth = 1
		
	if (currentWeekday == 0 and currentDay == 1):
		count += 1
		
	currentWeekday = (currentWeekday+1) % 7
	currentDay += 1

print(count)