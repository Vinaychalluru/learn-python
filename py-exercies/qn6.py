# Question 6
# Level 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math


class CalcFormula():
    'I will calculate the formula -> Square root of [(2 * C * D)/H]'
    C = 50
    H = 30

    def __init__(self):
        pass

    def __del__(self):
        pass

    def getInp(self):
        inpStr = input('Enter a sequence of digits seperated by comma : ')
        self.inpList = list(inpStr.split(','))
        print(self.inpList)

    def getRes(self):
        finalRes = []
        for i in self.inpList:
            res = math.floor(
                math.sqrt((2 * CalcFormula.C * int(i)) / CalcFormula.H))
            finalRes.append(str(res))

        print(','.join(finalRes))


try:
    cf = CalcFormula()
    cf.getInp()
    cf.getRes()
except Exception as e:
    print('An Exception occured : ' + repr(e))
finally:
    print('Bye')
