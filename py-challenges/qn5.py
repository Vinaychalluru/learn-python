# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class StrOpr():
    __myHiddenStr = 'Str'

    def __init__(self):
        pass

    def __del__(self):
        pass

    def getString(self):
        self.__myHiddenStr = input('Enter a string : ')

    def printString(self):
        print('String in Upper case is %s' % str(self.__myHiddenStr).upper())


try:
    so = StrOpr()
    so.getString()
    so.printString()
except Exception as e:
    print('Encountered an exception ' + repr(e))
finally:
    print('Bye')
    pass
