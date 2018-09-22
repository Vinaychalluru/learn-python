import numpy
import cv2
# The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
# A NumPy array is a grid of values.
# They are similar to lists, except that every element of an array must be the same type.
# NumPy is a base library for most of the libraries
# Such as Pandas and OpenCV, an image processing library

l = [i for i in range(1, 10)]

arr = numpy.array(l)
arr = numpy.asarray(l)
print(arr)
print(type(arr))
# Maps a single dimensional array of 20 into 4 rows and 5 columns
n = numpy.arange(20)
n = n.reshape(4, 5)
# n = numpy.arange(19)
# n = n.reshape(4,5) # When you try to do this, you will be thrown a ValueError as below
# ValueError: cannot reshape array of size 19 into shape (4,5)

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

#  --  Indexing Slicing and Iterating a Numpy Array  --
n = numpy.arange(20).reshape(4, 5)
print("\n", n)
print(n[0:2])  # Prints the first two rows similar to nested lists
# Second and third column elements across all the rows using the Advanced Indexing
print(n[:, 1:3])

# Required n x n set
print(n[1:3, 3:5])

print(*[i for i in n])
print(*[i for i in n.T])  # Transpose of an array
print(*[i for i in n.flat])  # Return a flat iterator over an array.

l = [[j*i for j in range(0, 3)] for i in range(0, 5)]
narr = numpy.array(l)
print("\n", narr)
print(narr.T)

l2 = [[0, 1],
      [0, 1],
      [0, 1],
      [0, 1]
      ]
print("\n", l2)
narr = numpy.array(l2)
print(narr)
print(narr.T)

l3 = [[0],
      [0, 1],
      [0, 1, 2]
      ]
print(l3)
narr = numpy.array(l3)
print(narr)
print(narr.T)

print("\n", n.flat)
print(n.flatten)
print(type(n.flat))
print(type(n.flatten))

#  --  Stacking and Splitting Numpy Arrays  --  
# Arguments of hstack and vstack should be of the same dimensions
# Using the pixel details of an image as input
img = cv2.imread('../assets/sample-gray-5x3.png')
img_r_attach = numpy.hstack((img, img, img))
cv2.imwrite('../assets/sample-r-stack-out.png',img_r_attach)
img_v_attach = numpy.vstack((img, img, img))
cv2.imwrite('../assets/sample-v-stack-out.png',img_v_attach)
r_list = numpy.hsplit(img_r_attach,5)
v_list = numpy.vsplit(img_v_attach,9)
print(type(r_list), type(v_list))
# print(r_list)
# print(v_list)