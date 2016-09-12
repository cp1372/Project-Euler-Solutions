def isPalindrome(value):
	return str(value) == str(value)[::-1]
	
def isLychrelNumber(x,step):
	y = int( str(x)[::-1] ) + x
	if isPalindrome(y):
		return False
	if (step > 50):
		return True
	else:
		return isLychrelNumber(y,step+1)

lychrelNumbers = []

for x in range(1, 10000):
	if isLychrelNumber(x,0):
		lychrelNumbers.append(x)
print (len(lychrelNumbers))