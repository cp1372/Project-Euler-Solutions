'''Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.'''
threshold = 100000000

#Dynamic programming since if x div y then y has all of x's factors???
def factors(n):
	#generate a set from
	x = set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
	return x

def divisorTest(n):
	divisors = factors(n)
	for d in divisors:
		if (primeTable[d+n//d] == 0):
			return False
	return True
	

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

listOfPrimes = primes(threshold+threshold//30+1)
primeTable = [0 for x in range( threshold+threshold//30+1 )]
for n in listOfPrimes:
	primeTable[n] = 1

resultsTable = []
count = 1 #account for n=1, all other cases are even
for x in range(2, threshold+1, 2):
	if (primeTable[x+1] == 1 and primeTable[x/2+2] == 1):
		if (divisorTest(x) == True):
			count += x
print (count)