'''Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.'''
import math

upperBound = int ( math.sqrt(1929394959697989990) )
lowerBound = int ( math.sqrt(1020304050607080900) )

def testNumber(x):
	test = str(x)[0::2]
	if (test == '1234567890'):
		return True
	else:
		return False

answer = []
for x in range(lowerBound, upperBound, 10):
	candidate = x*x
	if (testNumber(candidate) == True):
		answer.append(x)
		break
	
print (answer)