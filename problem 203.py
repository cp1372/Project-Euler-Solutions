import math

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def choose(n, r):
	result = math.factorial(n) / ( math.factorial(r) * math.factorial(n-r) )
	return result

squaresOfPrimes = [n*n for n in primes(50)]
def sqf(x):
    for p in squaresOfPrimes:
        if x % p == 0: return False  
    return True	

uniqueNumbers = set()
for n in range(1,51):
	for r in range(0,n+1):
		uniqueNumbers.add( choose(n,r) )
		

squareFreeNumbers = []
for x in uniqueNumbers:
	if sqf(x):
		squareFreeNumbers.append(x)



print (sum(squareFreeNumbers), squareFreeNumbers)