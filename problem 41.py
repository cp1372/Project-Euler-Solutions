def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primesList = primes(987654322)

pandigitalSet = set()
answer = []
digitSet = set()
for n in primesList:

	pandigitalSet.add(str( len(str(n)) ))
	digitSet = set( str(n) )
	if (digitSet == pandigitalSet):
		answer.append(n)
		
print (answer)