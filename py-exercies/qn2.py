# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


print('Enter a number to find the factorial : ')
myInt = int(input())
print(myInt)
myRes = 1

for i in range(1, myInt + 1):
    myRes = myRes * i

print("Factorial of %d is %d" % (myInt, myRes))
