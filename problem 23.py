def divisorSum(n):
	x = list(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
	x.sort()
	x = x[:-1] #remove last element
	x = list(set(x))
	result = sum(x)
	return result

upperBound = 28124
abundantSums = [0 for x in range(2*upperBound)]
abundantIndex = []

for n in range(1, upperBound):
	result = divisorSum(n)
	if (result > n):
		abundantIndex.append(n)
	
for x in abundantIndex:
	for y in abundantIndex:
		abundantSums[x+y] = x+y
		
answer = 0
for n in range(1,upperBound):
	if (abundantSums[n] == 0):
		answer += n
		
print (answer)