# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Input Format

# The first line contains an integer,n, denoting the number of commert ands.
# Each line i of the n subsequent lines contains one of the commands described above.

import traceback
import re

try:
    n = int(input('Enter no of commands:'))
    commandList = []
    outList = []

    for i in range(n):
        commandList.append(input())

    for command in commandList:
        # Code can be improved with below
        # There would be no need for re.findall as 'cmd' can be used for comparison
        # cmd = command.split(" ")[0]
        # args = command.split(" ")[1:]
        if command == "print":
            print(outList)
            continue
        if command == "pop" and len(outList)!=0:
            outList.pop()
            continue
        if command == "sort":
            outList.sort()
            continue
        if command == "reverse":
            outList.reverse()
            continue
        if len(re.findall(r"append", command)) > 0:
            args = command.split(" ")
            outList.append(int(args[1]))
            continue
        if len(re.findall(r"insert", command)) > 0:
            args = command.split(" ")
            outList.insert(int(args[1]), int(args[2]))
            continue
        if len(re.findall(r"remove", command)) > 0:
            args = command.split(" ")
            outList.remove(int(args[1]))
            continue
except Exception as e:
    print('Encountered an exception: ', repr(e))
    traceback.print_exc()

# Another approach - The best considering the efficiency
# There is no need to go through multiple 'if' blocks to find the matching command

n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)