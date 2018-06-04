# Observed that autopep leaves two lines blank space before and after the function definition


def funcName(param1, param2):  # Function Definition
    'funcName Docstring - Documentation string of the function - Which is optional'
    # What the funcName is intended to do
    # Optional to return something
    return None


# Function Call
funcName(1, 2)
print(type(funcName(1, 2)))


def paramTest(myList):
    'paramTest - To show how Params are passed by Reference'
    # All parameters (arguments) in the Python language are passed by reference.
    myList.append(5)
    # return None


myList = [1, 2, 3, 4]

paramTest(myList)
# Params are passed by reference - So all the changes made to myList inside the function paramTest
# are reflecting outside of the functionc call
print(myList)

# Types of Arguments
# Required
# Keyword
# Default
# Variable-length


def fn_required_arg(param1, param2, param3):
    print(param1, param2, param3)


def fn_keyword_arg(param1, param2, param3):
    print(param1, param2, param3)


def fn_default_arg(param1, param2, param3='NA'):
    print(param1, param2, param3)


def fn_variable_arg(param1, param2, *param3):
    print(param1, param2)
    for p in param3:
        print(p)


fn_required_arg(10, 20, 30)
fn_keyword_arg(param2=20, param3=30, param1=10)
# fn_keyword_arg(param1=10, 20, 30) # SyntaxError: positional argument follows keyword argument
fn_default_arg(10, 20, 30)
fn_default_arg(10, 20)
fn_variable_arg(10, 20, 30)
fn_variable_arg(10, 20)
fn_variable_arg(10, 20, 30, 40, 50)


def sum(arg1, arg2): return arg1 + arg2


print('Sum of %d and %d is %d' % (10, 20, sum(10, 20)))

# Scope of the Variable
myVar = 123


def fn_scope_test_internal_var(myVar):
    myVar = 12345
    return


def fn_var_scope_test_var(myVar):
    myVar = 1234
    print('mVar in the local scope is : ', myVar)
    fn_scope_test_internal_var(myVar)
    print('myyList after test_internal is : ', myVar)


print()
print('mVar before calls - Global : ', myVar)
fn_var_scope_test_var(myVar)
print('mVar after calls - Global : ', myVar)

# Scope of the List Variable 
# Python has the concept of Mutable and Immutable objects. 
# An object like a string or integer is immutable - every change you make creates a new string or integer.
# Lists are mutable and can be manipulated in place. See below
myList = [1, 2, 3]


def fn_scope_test_internal(myList):
    myList.append(5)
    return


def fn_var_scope_test(myList):
    myList.append(4)
    print('myList in the local scope is : ', myList)
    fn_scope_test_internal(myList)
    print('myyList after test_internal is : ', myList)


print()
print('myList before calls - Global : ', myList)
fn_var_scope_test(myList)
print('myList after calls - Global : ', myList)



# Notes :
# Anonymous Functions
# Declaration uses 'lambda' instead of 'def'
# lambda has been dropped from Python. Also, map, filter and reduce
