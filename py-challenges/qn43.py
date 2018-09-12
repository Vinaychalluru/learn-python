# Question 43

# Question
# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

import re
inpStr = input('Enter a sequence of words seperated by space :')


def findDigit(str):
    searchObj = re.search(r'^\d+$', str)
    if searchObj:
        return str
    else:
        return None


digitsOut = [int(dig) for dig in [
    findDigit(s) for s in inpStr.split(' ')] if dig is not None]
print(digitsOut)

digitsOut2 = [dig for dig in [
    int(s) for s in inpStr.split(' ') if s.isdigit() is True]]
print(digitsOut2)

# Below macthes and prints all the groups that macthes the pattern - Return is a list with string type
print(re.findall(r'\d+', inpStr))
# Below returns null since the argument is considered as one single string
print(re.findall(r'^\d+$', inpStr))
