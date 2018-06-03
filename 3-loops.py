# Loop control statement - Chnages execution from Loop's normal sequence
# When execution leaves a scope, all automatic objects that were created in that scope are destroyed

# break - teminates the innermost / current loop and resumes execution at the next statement
# continue - skip the current loop, retest for its condition before reiteratin

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

# Iterating by sequence of the index
for i in range(len(wholeNum)):
    print(wholeNum[i])

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
# It is s null operation. Nothing happens when it executes
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
