def factors(n):
	#generate a set from 
	x = list(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
	return x
	
numDivisors = 0
summation = 0
m = 1

while (numDivisors < 501):
	summation += m
	numDivisors = len( factors(summation) )
	m = m+1