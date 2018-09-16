# Assertions
# An assertion is a sanity check. Programmers often place assert statements
# at the start of a function to check for valid input, and after a function call to check for valid output.
# Python evaluates the accompanying expression, which is hopefully true.
# If the expression is false, Python raises an AssertionError exception

import traceback

a = 1 
b = "3"

print(a + b)
# Uncomment the below line and run. Though the line above it should throw Exception, python does not throw
# because it looks for Syntax errors first and does not run the code
# Only when the sntax errors are fixed, code would be run and exception thrown

# print(int(1)
print(1 + 10)

def isAdult(age):
    assert(age > 18), 'You should be above 18 to be allowed'
    return 'Allowed'


# If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError.
# AssertionError exceptions can be caught and handled like any other exception using the try-except statement,
# but if not handled, they will terminate the program and produce a traceback.
def assert_example():
    print('Begin - assert_example')
    print('You are %s' % isAdult(28))
    print('You are %s' % isAdult(10))
    print('You are %s' % isAdult(20))


def assert_example_with_try():
    print('Begin - assert_example_with_try')
    try:
        print('You are %s' % isAdult(28))
        print('You are %s' % isAdult(10))
        print('You are %s' % isAdult(20))
    except Exception as e:
        print('Encountered an Exception - ' + repr(e))
        traceback.print_exc()
    finally:
        print('Traceback of the Exception is printed above')

# Standard Exceptions
# try - except - else
# try - except - finally
# The code in the else-block executes if the code in the try: block does not raise an exception.


def exception_example():
    print('Begin - exception_example')
    try:
        myFile = open('./assets/sample-file.txt', 'r')
        myFile.write('Good Day!')
        print('Since exception occurs in the above line, code below this line will not get executed')
    except IOError as e:
        print('Encountered IOError - ' + repr(e))
    else:
        print('Successfully written')
        myFile.close()


def exception_depth_example():
    print('Begin - exception_depth_example')
    try:
        myFile = open('./assets/test-file.txt', 'r')
        try:
            myFileInner = open('./assets/sample-file.txt', 'r')
            myFileInner.write('Good Day!')
        finally:
            myFileInner.close()
    except IOError as e:
        print('Encountered IOError - ' + repr(e))
        print('Exception occurred while processing - ' + e.filename)
    else:
        myFile.close()


# The sole argument to raise indicates the exception to be raised.
# This must be either an exception instance or an exception class (a class that derives from Exception).
# If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments
def exception_raise():
    print('Begin - exception_raise')
    try:
        raise RuntimeError('Something went wrong during Runtime')
    except Exception as e:
        print('Encountered an exception - ' + repr(e))
        traceback.print_exc()


exception_example()
print('')
exception_depth_example()
print('')
exception_raise()
print('')
assert_example_with_try()
print('')
assert_example()
