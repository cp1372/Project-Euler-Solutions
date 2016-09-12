import math

def choose(n, r):
	result = math.factorial(n) / ( math.factorial(r) * math.factorial(n-r) )
	return result

valueA = choose(60,20)
valueB = choose(70-60,0)
valueC = choose(70,20)

answer= (1-valueA*valueB/valueC)*7
			
print (answer)