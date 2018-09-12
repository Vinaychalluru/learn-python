# Question 9
# Level 2

# Question
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

print('Enter few lines to capitalize them : ')
resList = []
while True:
    inpStr = input() # To break, press enter on a blank line
    if inpStr:
        resList.append(inpStr.upper())
    else:
        break

for resString in resList:
    print(resString)