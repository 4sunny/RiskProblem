# https://www.reddit.com/r/explainlikeimfive/comments/2shh95/eli5markov_chain_monte_carlo_i_honestly_want_to/
from random import randint
import numpy
import matplotlib
import matplotlib.pyplot as plt
matrix = []


def randomTry(aDice, dDice, battleCount, aWin, dWin):
    aList = []
    dList = []
    aDub = aWin
    dDub = dWin
    while aDice > 0:
        aList.append(randint(1, 6))
        aDice -= 1

    while dDice > 0:
        dList.append(randint(1, 6))
        dDice -= 1
    aList = sorted(aList)[aDice - battleCount:]
    dList = sorted(dList)[dDice - battleCount:]

    while battleCount > 0:
        if aList[battleCount - 1] < dList[battleCount - 1]:
            return aDub, 1 + dDub
            break
        battleCount -= 1
    return 1 + aDub, dDub



def getWinRate(aDice, dDice, battleCount, aWin, dWin, tryCount):
     while tryCount > 0:
        aWin, dWin = randomTry(aDice, dDice, battleCount, aWin, dWin)
        tryCount -= 1
     print(aWin)
     print(dWin)
     return (aWin / (aWin + dWin))
'''
a = int(input())
b = int(input())
aWin = 0
dWin = 0
print(getWinRate(a,b,min(a,b), aWin, dWin, 500000))
'''
for a in range(1, 11):
    list = []
    for b in range(1, 11):
        aWin = 0
        dWin = 0
        list.append(getWinRate(a, b, min(a,b), aWin, dWin, 5000000))
        print(list)
    matrix.append(list)
print(matrix)