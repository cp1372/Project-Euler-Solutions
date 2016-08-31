import math
n = 1000
for a in range(1,n):
	for b in range(a,n):
		c = math.sqrt( (a*a)+(b*b) )
		if ( a+b+c) == 1000):
			print (a*b*c)