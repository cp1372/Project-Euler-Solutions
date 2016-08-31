prime = 0
num = 2000000 
primes = []
total = 0

for i in range(2,num):
	test = True
	for m in range(2, int(i**0.5)+1):
		if (i % m == 0):
			test = False
			break
	if test == True:
		primes.append(i)
		total+=i
