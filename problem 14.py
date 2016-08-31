
biggestChain = 0
biggestSeed = 0
for seed in range (1,1000000):
	
	n = seed
	chain = [seed]
	while n > 1:
		if n%2 == 0:
			n = n//2
		else:
			n = 3*n+1
			
		chain.append(n)
	if len(chain) > biggestChain:
		biggestChain = len(chain)
		biggestSeed = seed
print (biggestSeed)