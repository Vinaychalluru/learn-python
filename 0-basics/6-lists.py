
import random

myList = [1, 2.5, 'A', 'B', 'Happy']
myList2 = ['x', 'y', 'z']

del myList[1]  # You can delete an element if you know the index

myList3 = myList + myList2
print(myList3)
print(myList2 * 2)
print('A' in myList)

# Accessing the elements
alphaList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(alphaList[2])
print(alphaList[-2])  # Negative: Count from the end - Negative Indexing
print(alphaList[1:])  # Slicing fetched sections
print(alphaList[1:4]) # Prints list[1], list[2], list[3]
print(alphaList[:])
print(alphaList[:-3])
print(alphaList[-5:-1]) # While using negative index also, list processed from left to right
print(alphaList[-1:-5])

# Extended Slicing
# Consider a sequence or list any_sequence[i:j:k]; According to the documentation, "slice of any_sequence from i to j with step k"
fibo = [0,1,1,2,3,5,8,13,21,34,55,89,144,233]
print(fibo[0:10:2])
# Prints every fourth element from the list / sequence fibo
print(fibo[::4])

# Function Vs Method : The difference between a function and a method is that,
# A method is applied on/after an Object
# Whereas A function takes an Object as argument
# Built In Functions
myTuple = (1, 2, 3, 4)
print(myList == myList2)
print(list(myTuple))  # Converts a Tuple into a list
print(max(myList2), min(myList2), len(myList2))

# Build In Methods
myList.append('Me')
myList.append('A')
print(myList.count('A'))
myList.extend(myList2)

print('Before Pop : ', myList)
print('After pop, the element popped out is returned :' , myList.pop())
print('After pop, the element popped out is returned :' , myList.pop(3))
print(myList)
myList.insert(3,'Happy')
print('List after insert :', myList)
# Returns the lowest index in the list that obj appears
print(myList.index('A'))

myList.remove('A')  # Removes object ONLY at the lowest index it appears and save changes in place
myList.reverse()
myList2.sort()  # Use when all the elements are same data type. E.g.: either string type / a number type
newList = [20, 10, 1.5, 2]
newList.sort()
print(newList)
print("myList before shuffle is ", myList)
# Randomizes the items of a list in place. Returns None.
random.shuffle(myList)
print("myList after Shuffle is", myList)

# Nested List
myList.clear()
myList = ['Good',[2,0,2,0]]
print(myList[0])
print(myList[0][3])
print(myList[1][3])
l = [ [j*i for j in range(0,4)] for i in range(0,4)]
print(l)

# Printing second and third column elements across all the rows
# The same can be achieved on a numpy array using narr[:,1:3]
# Similar Advanced indexing syntax for a normal nested list slicing is not available
for i in range(len(l)) :
    print(*[l[i][j] for j in range(1,3)])

# eval
# Evaluate the given "source" argument/string which represents a Python expression
myList = [0,1,2,3,4,5]
eval("myList."+"reverse()")
print(myList)
