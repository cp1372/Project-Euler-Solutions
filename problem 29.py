import time
start = time.time()

setOfTerms = set()
for a in range(2,101):
	for b in range(2,101):
		setOfTerms.add(a**b)

print (len(setOfTerms))

print("Result generated in %s ms." % ("{0:.4f}".format((time.time()-start) * 100)))