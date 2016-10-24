value = 1
for n in range(1,101):
	value *= n

digits = str(value)

digitSum = 0
for n in digits:
	digitSum += int(n)
print (digitSum)