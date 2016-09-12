def isPentagonal(y):
	n = ((1+24*y)**0.5+1)/6
	if (n - int(n) == 0):
		return True
	else:
		return False

n = 144
answer = 0
while (True):
	hexagonal = n*(2*n-1)
	if (isPentagonal(hexagonal)):
		answer = hexagonal
		break

print (answer)