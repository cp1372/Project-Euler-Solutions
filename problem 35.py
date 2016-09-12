'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?'''

import time
start = time.time()

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
    
def testRotations(n):
	origin = str(n)
	length = len(origin)
	
	if length == 1: 
		return True
	
	#Generate and test the prime's rotations
	for x in range(0, length):
		index = origin[x:]+origin[:x]
		prime = numbers[ int(index) ]
		if prime == 0:
			return False
			
	return True

primesList = primes(1000000)
numbers = [0 for x in range(1000000)]
for n in primesList:
	numbers[n] = n

count = 0
for n in primesList:
	if testRotations(n) == True:
		count += 1
print (count)
print("Result generated in %s ms." % ("{0:.4f}".format((time.time()-start) * 100)))
