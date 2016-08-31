def factors(n):
	#generate a set from 
	x = list(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
	x.sort()
	
	prime = 0
	for i in range(1,len(x) ):
		num = x[i]
		test = True
		
		for m in range(2, int(num**0.5)+1):
			if (num % m == 0):
				test = False
		if test == True:
			prime = num
	return prime