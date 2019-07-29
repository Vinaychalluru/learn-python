# Print the Zen of Python
import this

# Progress Bar
from tqdm import tqdm
for i in tqdm(range(1000000)):
    pass

# Reverse a list
# NOTE : list.reverse() is about 8 to 10 times faster than list[::-1] slicing
a = [x for x in range(10)]
print(a[::-1])

# Remove all occurrences of an item from list
vowels = ('a','e','i','o','u')
elements = ['a','b','c','d','e','f','c','g','a','a','a','e','i','i','i','e','o','z','f','c','d',1,2,3,4,6,1,2,3,5,6,7,2,3]
elements.remove(2) # Removes only the first occurrence of 2
elements = [ x for x in elements if x not in vowels ]
def remove_numbers():
    for num in range(0,9):
        while num in elements:
            elements.remove(num)
remove_numbers()
print(elements)

# List and it's scope in a function with default argument
def f(x=[]):
    print(id(x), len(x))
    x+=[3]
    return sum(x)
    
print(f() + f() + f())

# Find the Execution time of small code snippets
# timeit(stmt="pass", setup="pass", timer=default_timer, number=default_number)
from timeit import timeit
print(timeit("bc = b.copy()", setup="b = [str(x) for x in range(10000)]", number=10000))
print(timeit("bc = b[:]", setup="b = [str(x) for x in range(10000)]", number=10000))
print(timeit("bc = b.copy()", setup="b = [x for x in range(10000)]", number=10000))
print(timeit("bc = b[:]", setup="b = [x for x in range(10000)]", number=10000))
