n = 1;
solved = False
while solved == False:
	listOf = []
	n += 1
	for x in range (1,7):
		test = list( str(x*n) )
		test.sort()
		listOf.append(test)
	
	solved = True
	for x in range(0, len(listOf)-1 ):
		solved = solved and (listOf[x] == listOf[x+1] )

print (n)