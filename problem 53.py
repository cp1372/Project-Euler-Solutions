import math

def choose(n, r):
	result = math.factorial(n) / ( math.factorial(r) * math.factorial(n-r) )
	return result

answer = []
for n in range(1,101):
	for r in range(1,n+1):
		value = choose(n,r)
		if (value > 1000000):
			answer.append(value)
			
print (len(answer))