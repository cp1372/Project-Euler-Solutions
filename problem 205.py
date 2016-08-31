import random

PeterWins = 0
TotalGames = 10005000

def simulatePeter():
	score = 0
	for x in range(1,10):
		roll = random.randint(1,4)
		score += roll
	return score

def simulateColin():
	score = 0
	for x in range(1,7):
		roll = random.randint(1,6)
		score += roll
	return score
	
for x in range(0,TotalGames):
	if ( simulatePeter() > simulateColin()):
		PeterWins += 1
print (PeterWins/TotalGames)