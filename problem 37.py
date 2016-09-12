'''The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
 Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.'''

import time
start = time.time()

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
    
def testTruncations(n):
	origin = str(n)
	length = len(origin)
	if length == 1:
		return False
		
	#Generate and test the prime's rotations
	for x in range(0, length):
		indexLeft = origin[x:]
		indexRight = origin[0:x+1]
		prime = numbers[ int(indexLeft) ]
		if prime == 0:
			return False
		prime = numbers[ int(indexRight) ]
		if prime == 0:
			return False	
	return True

primesList = primes(1000000)
numbers = [0 for x in range(1000000)]
for n in primesList:
	numbers[n] = n

count = 0
listOfSpecial = []
for n in primesList:
	if (testTruncations(n) == True):
		count += 1
		listOfSpecial.append(n)
	if count == 30:
		break
	
print (listOfSpecial)
print (sum(listOfSpecial))
print("Result generated in %s ms." % ("{0:.4f}".format((time.time()-start) * 100)))
