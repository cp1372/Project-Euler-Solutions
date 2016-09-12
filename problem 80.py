from decimal import *

getcontext().prec = 105

#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
irrationalSums = []
for x in range(1, 101):
	y = Decimal.sqrt(Decimal(x))
	
	if ( y - int(y) != 0 ):
		decimals = str(y).replace('.','',1)
		numbers = (list (map(int, decimals)))
		
		digitSum = 0
		for n in range(0, 100):
			digitSum +=  numbers[n]
			
		irrationalSums.append(digitSum)

print (sum(irrationalSums))