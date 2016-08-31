result = 0

for x in range(1,10000000):
	
	numbers = (list (map(int, list(str(x)))))
	
	digitSum = 0
	
	while (digitSum != 89 and digitSum != 1):
		digitSum = 0
		for n in numbers:
			digitSum +=  n*n
		numbers = (list (map(int, list(str(digitSum)))))
	
	if (digitSum == 89):
		result += 1
		
print ('done')	
print (result)