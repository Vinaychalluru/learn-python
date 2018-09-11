# Print function
# Read an integer n.
# Without using any string methods, try to print the following:
# 123...n

# Note that "..." represents the values in between.

n = int(input())

for i in range(1, n+1):
    print(i, end="")
else:
    print()

# Using sep
print(*range(1, n+1), sep='', end='\n')

# The below logic fails for n > 9
sum = 0
for i in range(1, n+1):
    sum = sum + i * (10**(n-i))

print(sum)
