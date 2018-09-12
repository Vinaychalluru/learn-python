# Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

res = ''
for i in range(2000, 3201):  # This way we are including 3200 to be validated
    if (i % 7 == 0 and i % 5 != 0):
        res = res + str(i) + ','
else:
    res = res[0:len(res)-1]
    # res = res[0:-1]
    print(res)

# Using lists
resList = []
for i in range(2000, 3201):
    if (i % 7 == 0 and i % 5 != 0):
        resList.append(str(i))
else:
    resList = ','.join(resList)
    print(resList)
