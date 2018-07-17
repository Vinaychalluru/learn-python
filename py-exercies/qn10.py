# Question 10
# Level 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

inpList = []
inpList = input('Enter few words seperated with space : ').split(' ')

inpList.sort()
print(' '.join(set(inpList)))

# s = input()
# words = [word for word in s.split(" ")]
# print " ".join(sorted(list(set(words))))
