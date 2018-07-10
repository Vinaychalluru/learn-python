# Assertions
# An assertion is a sanity check. Programmers often place assert statements
# at the start of a function to check for valid input, and after a function call to check for valid output.
# Python evaluates the accompanying expression, which is hopefully true.
# If the expression is false, Python raises an AssertionError exception


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
    finally:
        print('You need to see the Assert Traceback for more details')

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


exception_example()
exception_depth_example()
assert_example_with_try()
assert_example()
