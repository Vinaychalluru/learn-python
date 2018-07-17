# Question 7
# Level 2

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

import traceback


class GenArray():
    'I will generate an Array with place value of x * y'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.resArray = []
        self.multilist = [[]]

    def genArrayValue(self):
        for i in range(0, self.x):
            subArray = []
            for j in range(0, self.y):
                subArray.append(i*j)
            else:
                self.resArray.append(subArray)
        else:
            print(self.resArray)

    def genMultilist(self):
        self.multilist = [[0 for col in range(self.y)]
                          for row in range(self.x)]
        for i in range(self.x):
            for j in range(self.y):
                self.multilist[i][j] = i*j
        else:
            print(self.multilist)


try:
    x, y = input('Enter two numbers :').split(',')
    ga = GenArray(int(x), int(y))
    ga.genArrayValue()
    ga.genMultilist()
    # input_str = input('Enter two numbers : ')
    # dimensions = [int(x) for x in input_str.split(',')]
    # rowNum = dimensions[0]
    # colNum = dimensions[1]
    # multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    # print(multilist)

    # for row in range(rowNum):
    #     for col in range(colNum):
    #         multilist[row][col] = row*col

    # print(multilist)
except Exception as e:
    traceback.print_exc()
