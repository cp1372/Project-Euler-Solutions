def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
    

listOfFourPrimesNumbers = []

maxPrime =  200000/(2*3*5)
validFactors = primes(maxPrime)

for n in range(2*3*5*7,200000):
	
	numPrimeFactors = 0
	for m in validFactors:
		if (n % m == 0):
			numPrimeFactors += 1
		if  (numPrimeFactors > 4 or m >= n):
			break
	if (numPrimeFactors == 4):
		listOfFourPrimesNumbers.append(n)

for x in range(0, len(listOfFourPrimesNumbers)-1-3):
	if (listOfFourPrimesNumbers[x]+1 == listOfFourPrimesNumbers[x+1] and listOfFourPrimesNumbers[x+1]+1 == listOfFourPrimesNumbers[x+2] and listOfFourPrimesNumbers[x+2]+1 == listOfFourPrimesNumbers[x+3]):
		print (listOfFourPrimesNumbers[x])
	