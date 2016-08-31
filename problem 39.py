import math
validList = []
p = 1001

for a in range (1,p):
	for b in range (1,p):
		
		c =  math.sqrt(a*a+b*b)
		test = ( c - int (c) == 0)
		
		if (test == True and ( a+b+c < 1001)):
			perimeter = a+b+c
			validSolution = (a,b,c,perimeter)
			validList.append(validSolution)

bestPerimeters = []
for x in range(0, 1001):
	bestPerimeters.append(0)


for x in validList:
	bestPerimeters [ int(x[3]) ] +=1
	
best = (max (bestPerimeters) )

print (bestPerimeters.index(best) )

		

