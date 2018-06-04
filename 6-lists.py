
myList = [1, 2.5, 'A', 'B', 'Happy']
myList2 = ['x', 'y', 'z']

del myList[1]  # You can delete an element if you know the index

myList3 = myList + myList2
print(myList3)
print(myList2 * 2)
print('A' in myList)

# Accessing the elements
alphaList = ['A', 'B', 'C', 'D']
print(alphaList[2])
print(alphaList[-2])  # Negative: Count from the end
print(alphaList[1:])  # Slicing fetched sections

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

myList.remove('A')  # Removes object
myList.reverse()
myList2.sort()  # Use when all the elements are either string type / a number type
newList = [20, 10, 1.5, 2]
newList.sort()
print(newList)
