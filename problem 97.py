base = 1
for x in range(0,7830457):
	base *= 2
	base %= 10000000000
	
result = ((28433*base) + 1) % 10000000000
print (result)