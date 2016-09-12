import time
start = time.time()

coins = [1,2,5,10,20,50,100,200]

print (coins)

def makeChange(money, numCoins):
	
	if (numCoins == 1):
		return 1
	s = 0
	
	for x in range(0,numCoins):
		remain = money-coins[x]
		if remain == 0:
			s += 1
		if remain > 0:
			s = s+makeChange(remain,x+1)
	return s
	
print ( makeChange(200,len(coins))  )

print("Result generated in %s ms." % ("{0:.4f}".format((time.time()-start) * 100)))