def isPalindrome(value):
	return str(value) == str(value)[::-1]

palindromes = []
for x in range(999,99,-1):
	for y in range (x, 99, -1):
		product = x*y
		if isPalindrome(product):
			palindromes.append(product)
print (max(palindromes))