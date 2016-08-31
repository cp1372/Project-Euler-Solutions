def isPalindrome(value):
	return str(value) == str(value)[::-1]
	
palindromes = []
for x in range(1,1000000):
	binaryRep = bin(x)[2:] 
	if isPalindrome(x) and isPalindrome(binaryRep):
		palindromes.append( (x,binaryRep) )
print (palindromes)

summation = 0
for x in palindromes:
	summation += x[0]
print (summation)