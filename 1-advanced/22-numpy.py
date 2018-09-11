import numpy
# The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
# A NumPy array is a grid of values.
# They are similar to lists, except that every element of an array must be the same type.

l = [i for i in range(1, 10)]

arr = numpy.array(l)
print(arr)

# The second argument (float) can be used to set the type of array elements.
arr = numpy.array(l, float)
print(arr)

arr = numpy.array(l, str)
print(arr)

# arr = numpy.array(l.reverse(), float) # This line will return nan to arr
# So, first reverse the list and then use it
l.reverse()
arr = numpy.array(l, float)
print(arr)