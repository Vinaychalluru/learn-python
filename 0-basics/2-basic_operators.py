# Operands and Operators

n1 = 8
n2 = 3
n3 = n1**n2
print(str(n1) + ' to the power of ' + str(n2) + ' is ' + str(n3))
print(n1, ' to the power of ', n2, ' is ', n3)
print('%d to the power of %d is %d' % (n1, n2, n3))
print(f"{n1} to the power of {n2} is {n3}")


n4 = n1/n2 # Float Division
n5 = n1//n2 # Integer Division (or) Floor Division - Digits after the decimal in the quotient are removed
print('Division gives ', n4)
print('Integer division (or) Floor division gives ', n5)

if(n1 != n2):
    print('Not Equal')
elif(n1 < n2):
    print('n1 < n2')
else:
    print('n1 >= n2')

# and / or

if (10 > 5 and 10 < 20):
    print('if AND')

if (10 > 20 or 20 > 10):
    print('if OR')


# Bitwise Operators
n1 & n2
n1 | n2
n1 ^ n2  # XOR
~n1  # Ones complement
n1 << 2  # Left Shift
n2 >> 2  # Right Shift

# Membership Operators - Test the membership in a sequence
# in, not in
myList = [1, 2, 3, 4, 5, 6, 7]
if n2 in myList:
    print('n1 in myList')
else:
    print('n1 not in myList')

# Identity Operators - Compares the memory locations of two objects
# is, is not
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location
n1 = 9
id_n1 = id(n1)  # id() returns the identity of an object
print('Identity / Memory location of n1 ', id_n1)
a = 10
b = 10
c = d = 10
if a is b:
    print('a is b')
else:
    print(id(a), 'is not', id(b))

if c is d:
    print('c is d')
    print('Id of c - %d, Id of d - %d' % (id(c), id(d)))

l = [1, 2, 3]
l1 = [1, 2, 3]
print("Check if l is l1 :", l is l1)

var = 100
if (var == 100):
    print('Value of expression is 100')
