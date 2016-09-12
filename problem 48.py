summation = 0
for n in range(1,1001):
	product = n
	for m in range(1,n):
		product *= n
		product %= 10000000000
	summation += product 
	summation %= 10000000000
print (summation)