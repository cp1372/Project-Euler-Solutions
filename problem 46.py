import time
start = time.time()

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
	

primesList = primes(50000)
result = set()
squareList = []

composites = set()

for x in range(3,20008,2):
	composites.add(x)

for x in range (1,100):
	squareList.append(2*x*x)

for n in primesList:
	for m in squareList:
		result.add(n+m)

primesSet = set(primes(20008))

	
print (composites - result - primesSet)


print("Result generated in %s ms." % ("{0:.4f}".format((time.time()-start) * 100)))