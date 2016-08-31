import math
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

specialNumbers = []
threshold = 10*(9**5)
for x in range(2,threshold):
	
	numbers = (list (map(int, list(str(x)))))
	digitSum = 0
	
	for n in numbers:
		digitSum +=  n**5
	if (digitSum == x):
		specialNumbers.append(x)
print (sum(specialNumbers))

