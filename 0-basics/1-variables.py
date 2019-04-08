# Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory.

# Do not need explicit declaration
# Declaration happens when you assign a value
# Variable Names are Case senstivie

counter = 100
Counter = 200
miles = 35.5
name = 'John'

print(counter)
print(Counter)
print(miles)
print(name)
print()

# Python has the concept of Mutable and Immutable objects.
# An object like a string or integer is immutable - every change you make creates a new string or integer.
# Lists are mutable and can be manipulated in place

# Multiple assignment
# An integer object is created with the value 100,
# and all three variables are assigned to the same memory location
# Observe how the memory location of the variable 'a' does not change
# until its value changes
a = b = c = 100
print('Values are a - %d, b - %d, c - %d' % (a, b, c))
print('Ids of a - %d, b - %d, c - %d' % (id(a), id(b), id(c)))

c = 200
print('Values are a - %d, b - %d, c - %d' % (a, b, c))
print('Ids of a - %d, b - %d, c - %d' % (id(a), id(b), id(c)))

a, b, c = 100, 100, 'john'
print('Values are a - %d, b - %d, c - %s' % (a, b, c))
print('Ids of a - %d, b - %d, c - %d' % (id(a), id(b), id(c)))

a, b, c = 100, 200, 'john'
print('Values are a - %d, b - %d, c - %s' % (a, b, c))
print('Ids of a - %d, b - %d, c - %d' % (id(a), id(b), id(c)))


# Integer objects can be deleted as below
del a, b, c

# Strings
msg = 'Ya Hello buddy'

print()
print(msg[0])  # Index start at 0
print(msg[3:8])  # Slice Operator [:]
print(msg[3:])
print(msg + msg)
print(msg * 2)

# Lists
# All elements of a list can be of different data type
# Use slice operator to access the elements
myList = ['abcd', 786, 2.23, 'Where are you', 70.2]
print(myList)
myList[0] = 'xyz'
print(myList)

# Tuples
# Can be thought of as a read-only lists
# Enclosed within parentheses
# Unlike lists, elements and size of a tuple can't be changed
myTuple = ('ab', 786, 2.23, 'john', 70.2, 200)

# Dictionaries
# Enclosed within Curly Braces
# No order. Elements are unordered
myDict = {}
myDict['one'] = 'This is one'
myDict[2] = 'This is two'

tinyDict = {
    'name': 'john',
    'code': 6734,
    'dept': 'sales'
}

print(myDict)
print(tinyDict.keys())
print(tinyDict.values())

# Data Type Conversion
print(int('10'))
print(chr(65))  # A is printed in the output
print(str(10))

# The Underscore
# Underscore _ is considered as "I don't Care" or "Throwaway" variable in Python
# The python interpreter stores the last expression value to the special variable called _.

# Try the below in an Interpreter mode
# print(10)
# _
# _ ** 3

# The underscore _ is also used for ignoring the specific values.
# If you don’t need the specific values or the values are not used, just assign the values to underscore
(x, _, y) = (1, 2, 3)
print(x, y)

# 1. For storing the value of last expression in interpreter.
# 2. For ignoring the specific values. (so-called “I don’t care”)
# 3. To give special meanings and functions to name of vartiables or functions.
# 4. To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.
# 5. To separate the digits of number literal value.

# The Star
print(*range(1,10))
