digitLength = [0 for x in range(1001)]
groupings = []

for x in range (1,1000):
	for y in range (1,1000):
		z = x**y
		digits = len(str(z))
		if (digits > y):
			break
		if (digits == y):
			digitLength[y] += 1
			groupings.append( (x,y,z) )
			
print ( sum(digitLength) )
print (groupings)