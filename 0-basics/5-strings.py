# Python does not support a character type
# Considered as strings of length One

myStr = 'Good Morning. How are you doing'
mySubStr = myStr[0:5]
mySlice = myStr[14:]
mySliceCopy = mySlice

print('mySubStr :', mySubStr)
print('mySlice : ', mySlice)

# String Operations
myStr = 'String'
print(myStr + myStr)
print(myStr * 4)
print(myStr[0:3])
print('r' in myStr)
print('v' in myStr)
print('v' not in myStr)

# String Formatting
myName = 'Vinay'
myYear = 1990
myFmtStr = 'Hello %s. Keep learning'
print('String formatting is done using the %')
print(myFmtStr % myName)
print('I am %s I am born in %d' % (myName, myYear))

paraStr = """Non-printable characters such as
TAB (\t) will show up as they intended to when displayed.
New lines within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(paraStr)

print('Test\\Path')
print(r'Test\\Path') # Printing a raw string
print(u'Unicode string uses 16-bit Unicode to store the strings')

# Built-In String Methods
myStr = 'STring meTHods'
mySubStr = 'ring'
print(myStr.capitalize())
print(myStr.swapcase())
print(myStr.center(50,'-'))
print(mySubStr in myStr)
print(myStr.count(mySubStr)) # Retuns no of times
print(myStr.count('dummy'))
print(myStr.endswith(mySubStr))
print(myStr.startswith(mySubStr))
print(myStr.find(mySubStr)) # Returns index if found / -1 if not
print(myStr.find('dummy'))
print(myStr.index(mySubStr)) # Raises an exception if not found

# There are few validation methods available. Explore
# Ex : myStr.isalpha() myStr.islower() max(myStr) min(myStr)

print(myStr.join('^$'))
print(len(myStr))
print('        Spaces at the start are stripped                 '.lstrip())
print('        Spaces at the end are stripped                 '.rstrip())
print('        Extra Spaces     at start and end stripped                 '.strip())
print(myStr.split())
print(myStr.zfill(20)) # Left padded with zeroes upto specified length

