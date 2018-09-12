# Question 12
# Level 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

import traceback
allDigitsEven = []
allDigitsEvenStr = ''


def splitDigits(x):
    nbrSplit = []
    while x > 0:
        nbrSplit.append(int(x % 10))
        x = x // 10
    else:
        return nbrSplit


def findAllDigitsEven(x):
    allEvenFlag = True
    nbrSplit = splitDigits(x)
    for d in nbrSplit:
        if d % 2 != 0:
            allEvenFlag = False
            break
    if allEvenFlag == True:
        allDigitsEven.append(x)


def findAllDigitsEven_Shorter(x):
    xOrig = x
    allEvenFlag = True
    global allDigitsEvenStr
    while x > 0:
        if ((x % 10) % 2) != 0:
            allEvenFlag = False
            break
        x = x // 10
    else:
        if allEvenFlag == True:
            allDigitsEvenStr = allDigitsEvenStr + str(xOrig) + ','

try :
    for nbr in range(1000, 3001):
        findAllDigitsEven(nbr)
    else:
        print(allDigitsEven)

    for nbr in range(1000, 3001):
        findAllDigitsEven_Shorter(nbr)
    else:
        allDigitsEvenStr = allDigitsEvenStr[0:-1]
        print(allDigitsEvenStr)
except Exception as e:
    print(traceback.print_exc())