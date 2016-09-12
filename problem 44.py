pentagonalNumbers = []
for n in range(1,2501):
	pentagonalNumbers.append( (n*(3*n-1))//2 )
	
upperBound = 2*((2501*(3*2501-1))//2)+1

pentagonTable = [0 for x in range(0, upperBound)]
for n in pentagonalNumbers:
	pentagonTable[n] = 1

answerList = []

for a in pentagonalNumbers:
	for b in pentagonalNumbers:
		if (pentagonTable[b+a] == 1 and pentagonTable[b-a] == 1 ):
			answerList.append( [b,a,abs(b-a)] )

print (answerList)