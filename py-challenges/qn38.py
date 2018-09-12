# Question 38
# Level 1

# Question:
# Write a program to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10] using ListComp

intList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNbrSquares = [x**2 for x in intList if x % 2 == 0]
print(evenNbrSquares)
