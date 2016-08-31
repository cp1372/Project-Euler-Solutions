def divisorSum(n):
	x = list(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
	result = sum(x)-n
	return result


listOfdivisorSums = []

for n in range(1, 10000):
	result = divisorSum(n)
	if (result != n and divisorSum(result) == n):
		listOfdivisorSums.append(n)
		
print (listOfdivisorSums)

	