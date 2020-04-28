#https://www.reddit.com/r/explainlikeimfive/comments/2shh95/eli5markov_chain_monte_carlo_i_honestly_want_to/
from random import randint
aDice = int(input())
dDice = int(input())
battleCount = min(aDice,dDice)
tryCount = 100000
aWin = 0
dWin = 0

def randomTry(aDice, dDice, battleCount, aWin, dWin):
	aList = []
	dList = []
	aDub = aWin
	dDub = dWin
	while aDice > 0:
		aList.append(randint(1,6))
		aDice -= 1
	
	while dDice > 0:
		dList.append(randint(1,6))
		dDice -= 1
	aList = sorted(aList)[aDice - battleCount:]
	dList = sorted(dList)[dDice - battleCount:]
	print(aList)
	print(dList)
	
	while battleCount > 0:
		if aList[battleCount - 1] > dList[battleCount - 1]:
			aDub += 1
		else:
			dDub += 1
		battleCount -= 1
	return aDub, dDub
while tryCount > 0:
	aWin, dWin = randomTry(aDice, dDice, battleCount, aWin, dWin)
	tryCount -= 1
	
print(aWin/ (aWin + dWin))
