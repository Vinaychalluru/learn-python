# Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory.

# Do not need explicit declaration
# Declaration happens when you assign a value

counter = 100
miles = 35.5
name = 'John'

print(counter)
print(miles)
print(name)
print()

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


# Integer object and can be deleted as below
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
print(chr(8))
print(str(10))
