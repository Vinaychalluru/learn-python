# Modifier & Description
# re.I | Performs case-insensitive matching.
# re.L | Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B).
# re.M | Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
# re.S | Makes a period (dot) match any character, including a newline.
# re.U | Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.
# re.X | Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.

import re

myStr = 'I am a string to be searched for regular expression patterns'

matchObj = re.match(r'^I AM a STRING', myStr, re.M|re.I)
if matchObj:
    print(matchObj.group())

myStr = 'I am one SEP I am two SEP I am three'

searchObj = re.search(r'(.*) SEP (.*?) .*', myStr, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

myStr = 'I am one SEP I am two'

searchObj = re.search(r'(.*) SEP (.*?) .*', myStr, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

# Matching Versus Searching
# Python offers two different primitive operations based on regular expressions: 
# match checks for a match only at the beginning of the string, 
# search checks for a match anywhere in the string

myStr = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', myStr, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!")

searchObj = re.search(r'dogs', myStr, re.M | re.I)
if searchObj:
    print("search --> searchObj.group() : ", searchObj.group())
else:
    print("Nothing found!")
    
myStr="ABC123 abc 123 def456 789xyz"
reList=re.findall(r'[a-zA-Z]+[0-9]+',myStr)
print("Output of re.findall() :", *reList,sep='\n',end='\n')

myStr="12,34,56,78.90"
print('Output of re.split() :')
print(*re.split(r'[,.]',myStr),sep='\n',end='\n')

myStr="Alpha beta Alpha charlie Alpha donna"
reList=re.findall(r'Alpha',myStr)
print("Output of reList :", *reList, sep="\n", end="\n")

# finditer retuns a match object
reIterList=re.finditer('Alpha',myStr)
print(*[(reObj.start(),reObj.end()) for reObj in reIterList],sep="\n",end="\n")