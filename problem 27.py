def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primeList = primes(100000)

tableSize = max(primeList)+1
primesTable = [0 for x in range(tableSize)]
for n in primeList:
	primesTable[n] = 1
	
answers = []
for a in range(-999,1000):
	for b in range(-1000,1001):
		count = 0
		for n in range(0, abs(b)+1):
			y = (n*n+a*n+b)
			
			if (primesTable[y] == 1):
				count += 1
			else:
				break
			
		if (count > 1):
			answers.append( (a,b,count) )

result = (0,0,0)
for n in answers:
	if (n[2] > result[2]  ):
		result = n
		
print (result)
print (result[0]*result[1])