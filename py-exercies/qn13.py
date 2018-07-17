# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

import re

no_of_digits = 0
no_of_letters = 0

def countAlphaNum(inpStr):
    global no_of_digits
    global no_of_letters
    digits = re.findall(r'\d',inpStr)
    no_of_digits = len(digits)
    letters = re.findall(r'[a-zA-Z]',inpStr)
    no_of_letters = len(letters)

countAlphaNum(input('Input a sentence to count :'))
print('LETTERS', str(no_of_letters))
print('DIGITS', str(no_of_digits))

# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])
