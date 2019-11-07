# Loop control statement - Changes execution from Loop's normal sequence
# When execution leaves a scope, all automatic objects that were created in that scope are destroyed

# break - teminates the innermost / current loop and resumes execution at the next statement
# continue - skip the current loop, retest for its condition before reiterating

count = 10

while (count < 5):  # If the condition is false, the loop will never run
    print(str(count))
    count += 1


# Python allows to have an else statement associated with a loop statement

while (count > 5):
    print(str(count))
    count -= 1
else:
    print('Else for the While loop')

wholeNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
# The else statement is executed when the condition becomes false. Loop will not run further
while (wholeNum[i] % 2 == 0 and i < 10):
    i += 1
    print('i = ', i)
else:
    i += 1
    print('Else for the While loop')
    print('i = ', i)

for l in 'Alpha':
    print('Letter is :', l)

for num in wholeNum:
    print('Num :', num)

print(*wholeNum,sep='\n')

# Iterating by sequence of the index
for i in range(len(wholeNum)):
    print(wholeNum[i])

# Using step value for range()
for i in range(len(wholeNum) -1 ,0,-1):
    print(wholeNum[i])

# Using parameter 'end' and 'sep' for print()
for i in range(1,11):
    print(i,end="~")
else:
    print()

# The print function uses sep to separate the arguments, and end after the last argument
# * is used to pass all the values of range as arguments to print
print(*range(1,11),sep='',end='\n')

# Using _ in the loops
# Underscore _ is considered as "I don't Care" or "Throwaway" variable in Python
# It just indicates that the loop variable isn't actually used
for _ in range(0,5):
    print()

lower = 10
upper = 20
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:  # The else statement is executed when the loop has exhausted iterating the list.
        print('%d is a prime number \n' % (num))

# Pass statement
# It is a null operation. Nothing happens when it executes
# Useful in places where your code will go but has not been written yet
for letter in 'Congratulations':
    if letter == 'u':
        pass
        print('This is pass block')
    print('Current Letter :', letter)

for letter in 'Congratulations':
    if letter == 'u':
        continue
        print('This is continue block') # This line would be unreachable
    print('Current Letter :', letter)
