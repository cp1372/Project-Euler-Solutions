oddNum = {'1','3','5','7','9',}

def isReversible(value):
	
	if (value % 10 == 0):
		return False
		
	y = int(str(value)[::-1])
	n = x+y
	numbers = set( str(n) )
	if ( numbers.issubset(oddNum) ):
		return True
	return False
	

count = 0
#for x in range(1,1000):
for x in range(1,1000000000):
	if isReversible(x):
		count += 1

print (count)