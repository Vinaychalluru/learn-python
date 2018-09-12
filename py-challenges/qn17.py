# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

totalB = 0

while True:
    inp = input()
    if inp:
        inpTxn = inp.split(' ')
        if inpTxn[0] == 'D':
            totalB = totalB + int(inpTxn[1])
        elif inpTxn[0] == 'W':
            totalB = totalB - int(inpTxn[1])
        else:
            pass
    else:
        break

print(totalB)
