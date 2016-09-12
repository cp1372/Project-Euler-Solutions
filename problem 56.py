import time
start = time.time()

def digitSum(x):
	numbers = (list (map(int, list(str(x)))))
	digitSum = 0
	for n in numbers:
		digitSum +=  n
	return digitSum

listOfNumbers = []
for a in range(2,100):
	for b in range(2,100):
		listOfNumbers.append(a**b)

answer = 0
for x in listOfNumbers:
	answer = max(answer, digitSum(x) )

print (answer)	
print("Result generated in %s ms." % ("{0:.4f}".format((time.time()-start) * 100)))