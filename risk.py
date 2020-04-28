import time
import itertools
diceAtt = int(input("Number of dice attacker"))
diceDef = int(input("Number of dice defender"))
start_time = time.time()
diceNum = []
for n in range(6):
    diceNum.append(n+1)
AttSet = list(map(list, itertools.product(diceNum, repeat=diceAtt)))
DefSet = list(map(list, itertools.product(diceNum, repeat=diceDef)))
AttWin = 0
DefWin = 0
for x in range(len(AttSet)):
    for y in range(diceAtt):
        AttSet[x].sort()
for x in range(len(DefSet)):
    for y in range(diceDef):
        DefSet[x].sort()
for x in range(len(AttSet)):
    for y in range(len(DefSet)):
        if AttSet[x][-1] > DefSet[y][-1]:
            AttWin += 1
        else:
            DefWin += 1
        if len(AttSet[x]) > 1 and len(DefSet[y]) > 1:
            if AttSet[x][-2] > DefSet[y][-2]:
                AttWin += 1
            else:
                DefWin += 1
print("Likelihood of attacker winning: "+str(100/(AttWin/DefWin + 1) * AttWin/DefWin))
print("Overall attacker wins: "+str(AttWin))
print("Overall defender wins: "+str(DefWin))
print("--- %s seconds ---" % (time.time() - start_time))