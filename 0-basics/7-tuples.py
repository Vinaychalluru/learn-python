
myTup = (100, 10.5, 'A', 'Alpha')
# To write a tuple containing a single value you have to include a comma, even though there is only one value
myTup2 = (100,)

an_int = (100)
print(type(an_int)) # It would be an int. Not a tuple

# All the methods and functions that are used on lists are applicable on Tuples
# ..except that we can not update or edit the elements
# So, myTup.append() or myTup.remove() or myTup.pop() or myTup.extend() is invalid
# Yet, you can delete an entire tuple
del(myTup2)

print(len(myTup))
print(myTup * 3)
print(myTup + myTup)
print(myTup.index('A'))