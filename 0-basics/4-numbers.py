# Number data types are immutable.
# Changing the value of number data type results in a newly allocated object

import math
import random

var1 = 10
del var1  # To delete the reference to a number object

x = 4
y = 2
f = 20.46489

print("Absolute is ", abs(x))
print("Fabs is ", math.fabs(x))  # Returns a float
print("Power to 3 is", math.pow(x, 3))
print("Square Root is ", math.sqrt(x))
print("Exponential is ", math.exp(x))
print("Natural logarithm is ", math.log(x))
print("Max is ", max(x, y))  # Max in a tuple
print("Min is ", min(x, y))  # Min in a tuple

print("Ceil is ", math.ceil(f))
print("Floor is ", math.floor(f))
print("Round is ", round(f))
print("Round to 2 decimal is ", round(f, 2))
# Returns the fractional and integer parts as two-item tuple
print("Modf is ", math.modf(f))

# Random Number Functions

myTuple = (10, 20, 30, 40, 50)
myList = [100, 200, 300, 400, 500]
x = 100
y = 200

# A random item from a list, tuple, or string.
print("Choice is ", random.choice(myTuple))
# A randomly selected element from range(start, stop, step)
print("Randrange is ", random.randrange(x, y, 3))
# A random float r, such that 0 is less than or equal to r and r is less than 1
print("Random is", random.random())
# A random float r, such that x is less than or equal to r and r is less than y
print("Uniform(x,y) is ", random.uniform(x, y))

# Sets the integer starting value used in generating random numbers. Call this function before calling any other random module function such that you can simulate to generate the same random number when executed. Returns None.
random.seed(x)
print("Seed is set to ", x)

print("myList before shuffle is ", myList)
# Randomizes the items of a list in place. Returns None.
random.shuffle(myList)
print("myList after Shuffle is", myList)

# math module has functions that perform trigonometric calculations
# Also, mathematical constants pi and e are available

print(math.pi, math.e)
