# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# import math
inpNbr = int(input('Enter a single digit number : '))
sum = 0

for i in range(0,5):
    for j in range(0,i):
        # sum = sum + inpNbr * math.pow(10,j)
        sum = sum + inpNbr * 10**j

# print(int(sum))
print(sum)