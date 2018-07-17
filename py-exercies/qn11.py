# Question 11
# Level 2

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

inpNbrs = [nbr for nbr in input(
    'Enter comma seperated 4 digit Binary numbers :').split(',')]
res = []
for iBinaryNbr in inpNbrs:
    iDecimalNbr = int(iBinaryNbr, 2)
    if iDecimalNbr % 5 == 0:
        res.append(iBinaryNbr)
else:
    print(','.join(res)) # Printing the result as a string rather than a list
