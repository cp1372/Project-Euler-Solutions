import math
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

specialNumbers = []
for x in range(3,1854722):
	
	numbers = (list (map(int, list(str(x)))))
	factorialSum = 0
	
	for n in numbers:
		factorialSum +=  math.factorial (n)
	if (factorialSum == x):
		specialNumbers.append(x)
print (sum(specialNumbers))