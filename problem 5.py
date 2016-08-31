def findLcm(a,b):
	lcm = 0
	hcf = 0
	i = 1
	greater = max(a,b)
	
	while (i < greater):
		if (a%i == 0 and b%i == 0):
			hcf = i
		i+=1
	lcm=(a*b)/hcf;
	return lcm;

lcm = 1
for x in range(2,21):
	lcm = findLcm(lcm,x)
print (lcm)