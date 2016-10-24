#Problem 1 is basically FizzBuzz so why not do both
n = 100
for x in range(1,n):
	if (x%15 == 0):
		print 'Fizz Buzz'
	elif (x%5 == 0):
		print 'Buzz'
	elif (x%3 == 0):
		print 'Fizz'
	else:
		print x