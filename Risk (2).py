
aDice = int(input())
dDice = int(input())
diceFace = 6
aListNominators = []
dListNominators = []
aTotalPossibilities = diceFace ** aDice
dTotalPossibilities = diceFace ** dDice
'''
if aDice == 1:
	n = 0
	aAmount = 0
	while n < 5:
		aAmount += n**dDice
	'''
	
def getTotalOccurences(diceCount, n):
	if diceCount == 1:
		return 1
	else: 
		power = diceCount - 1
		f = 0
		total = 0
		while f < diceCount:
			total += n**(power) * (n-1)**f
			f += 1
			power -= 1
		return total

def getOccurenceForSide(aDice, dDice):
	a = 1
	while a < 7:
		b = getTotalOccurences(aDice, a)
		c = getTotalOccurences(dDice, a)
		aListNominators.append(b)
		dListNominators.append(c)
		a += 1
		

def debug(whichSide):
	WinPercentage = 0
	if whichSide == "A":
		winChance = dTotalPossibilities 
		for x in range(diceFace -1, -1, -1):
			aFraction = str(aListNominators[x]) + "/" + str(aTotalPossibilities)
			if aDice == 1 and dDice == 1:
				winChance = x
			else:
				winChance -= dListNominators[x]
			print("Attacker has a {} chance to roll {}, which has a {} chance of winning".format(aFraction, x + 1, str(winChance) + "/" + str(dTotalPossibilities)))
			WinPercentage += (aListNominators[x]/aTotalPossibilities) * (winChance/dTotalPossibilities) * 100
		print("Attacker is " + str(WinPercentage) + "% likely to win")
		print((aDice))
		print(diceFace)
	else:
		aListNominators.append(0) #so it delays the chance decrease
		winChance = aTotalPossibilities
		for x in range(diceFace -1, -1 , -1):
			dFraction = str(dListNominators[x]) + "/" + str(dTotalPossibilities)
			if aDice == 1 and dDice == 1:
				winChance = x + 1
			else:        
				winChance -= aListNominators[x + 1]
			print("Defender has a {} chance to roll {}, which has a {} chance of winning".format(dFraction, x + 1, str(winChance) + "/" + str(aTotalPossibilities)))
			WinPercentage += (dListNominators[x]/dTotalPossibilities) * (winChance/aTotalPossibilities) * 100
		print("Defender is " + str(WinPercentage) + "% likely to win")
		print(WinPercentage/100 * (aTotalPossibilities + dTotalPossibilities))

#print(getTotalOccurences(aDice, dDice))
print(getOccurenceForSide(aDice, dDice))
print(debug("A"))


#def getWinPercent(aDice, dDice):

