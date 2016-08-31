n = 1000000
nextInteger = 1
fraction = str(nextInteger)

while (len(fraction) <= n):
	nextInteger += 1
	fraction += str(nextInteger)
	
product = 1
for x in range(1,6):
	product *= int( fraction[10**x-1] )
print (product)