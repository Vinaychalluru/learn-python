
# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# Python generators are a simple way of creating iterators. All the overhead we mentioned below are automatically handled by generators in Python
# There is a lot of overhead in building an iterator in Python; we have to implement a class with __iter__() and __next__() method, keep track of internal states, raise StopIteration when there was no values to be returned etc.

# Creation
# It is as easy as defining a normal function with yield statement instead of a return statement.
# If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function
# The difference is that, while a return statement terminates a function entirely,
# yield statement pauses the function saving all its states and later continues from there on successive calls.

# A generator function
# Generator function contains one or more yield statement.
# When called, it returns an object (iterator) but does not start execution immediately.
# Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.
# Unlike normal functions, the local variables are not destroyed when the function yields and resumes the execution where it was left off.
# Furthermore, the generator object can be iterated only once

# Why ?
# 1. Easy to implement than their counter part iterator class
# 2. Memory efficient
# Generators are especially useful for memory-intensive tasks, where there is no need to keep all of the elements of a memory-heavy list accessible at the same time. Calculating a series of values one-by-one can also be useful in situations where the complete result is never needed, yielding intermediate results to the caller until some requirement is satisfied and stop / pause further processing
# 3. Represent an Infinite stream
# 4. Pipeline Generators


def my_gen_func():
    'A simple generator function'
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Function is not called here. Run the program in DEBUG mode
my_generator = my_gen_func()

print(type(my_gen_func()))
print(type(my_generator))

# Iterating over the list and the generator looks completely the same.
# However, although the generator is iterable, it is not a collection, and thus has no length.
# Collections (lists, tuples, sets, etc) keep all values in memory and we can access them whenever needed.
# A generator calculates the values on the fly and forgets them, so it does not have any overview about the own result set.
# Exception is thrown when below line is executed -> TypeError: object of type 'generator' has no len()
# len(my_generator)
#

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
# Finally, when the function terminates, StopIteration is raised automatically on further calls
# print(next(my_generator))
# print(next(my_generator))

# We can use generators with for loops directly
# Furthermore, the generator object can be iterated only once. To iterate again, create another object
my_generator2 = my_gen_func()
for item in my_gen_func():
    print(item)


# A Good Example
# A 'Search Task', where typically there is no need to wait for all results to be found.
# The yield instruction should be put into a place where the generator returns an intermediate result to the caller and sleeps until the next invocation occurs
def search(keyword, filename):
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        if keyword in line:
            # If keyword found, return it
            yield line
    f.close()


the_generator = search('James', '../assets/sample-contacts.txt')
# We get the first search result without looking through the whole file
print(next(the_generator))
# The generator resumed on the last yield keyword/statement and went through the loop until it hit the yield keyword/statement again
# This call resumes where it was left off
print(next(the_generator))
print(next(the_generator))
print(next(the_generator))
print(next(the_generator))
# If the generator function does not hit the yield keyword/statement anymore, 
# it will raise a StopIteration exception (just like all iterable objects do when they are exhausted/finished)
# print(next(the_generator))

# Another Example
def hold_client(name):
    yield 'Hello, %s! You will be connected soon' % name
    yield 'Dear %s, could you please wait a bit.' % name
    yield 'Sorry %s, we will play a nice music for you!' % name
    yield '%s, your call is extremely important to us!' % name

# Normally, generator functions are implemented with a loop having a suitable terminating condition


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


for char in rev_str('Morning'):
    print(char)

# A Generator Expression creates an anonymous generator function
# Syntax is similar to that of a ListComp. But the square brackets are replaced with round parentheses
# The major difference between a ListComp and a generator expression is that,
# while ListComp produces the entire list, generator expression produces one item at a time on the fly
# They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient than an equivalent list comprehension

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)

square_gen = (x**2 for x in my_list)
print(next(square_gen))
print(next(square_gen))

# Generator expression can be used inside functions. When used in such a way, the round parentheses can be dropped
sum(x**2 for x in my_list)


# A normal function to return a sequence will create the entire sequence in memory before returning the result.
# This is an overkill if the number of items in the sequence is very large.

# Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.

# Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory and since generators produce only one item at a time, it can represent infinite stream of data.

def all_even():
    n = 0
    while True:
        yield n
        n += 2

def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr, prev + curr
        counter += 1

# Pipelining Generators
# A series of operations or function calls

# Suppose we have a log file from a famous fast food chain.
# The log file has a column (4th column) that keeps track of the number of pizza sold every hour
# We want to sum it to find the total pizzas sold in 5 years.

# with open('sells.log') as file:
#     pizza_col = (line[3] for line in file)
#     per_hour = (int(x) for x in pizza_col if x != 'N/A')
#     print("Total pizzas sold = ",sum(per_hour))
