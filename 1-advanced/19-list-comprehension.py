# List comprehension (ListComp)
# List comprehensions provide a concise way to create lists
# Always returns a result list 

# It consists of brackets containing an expression followed by a for clause, then
# zero or more for or if clauses. The expressions can be anything, meaning you can
# put in all kinds of objects in lists.

# The result will be a new list resulting from evaluating the expression in the
# context of the for and if clauses which follow it.

# Basic Syntax
# new_list = [expression(i) for i in old_list if filter(i)]
# *result* = [*transform* *iteration* *filter*]

# List of Squares
squares = []
for x in range(10):
    squares.append(x**2)

squares = [ x**2 for x in range(10)]

# Not Equal Elements from two lists
notEqualEle = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            notEqualEle.append((x, y))

# If the expression is a tuple (e.g. the (x, y)), it must be parenthesized.
notEqualEle = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(notEqualEle)

# Common elements
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num) # Output: [2, 3, 4]

# New list with the values doubled
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]

# Filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# Apply a function to all the elements
[abs(x) for x in vec]

# Call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# Create a list of 2-tuples like (number, square)
# The tuple must be parenthesized, otherwise an error is raised
[(x, x**2) for x in range(6)]

# Flatten a list using a ListComp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# Nested Listcomp
# The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# The following ListComp will transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

# The same 
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed

# In the real world, you should prefer built-in functions to complex flow statements. 
# The zip() function would do a great job for this use case:
list(zip(*matrix))