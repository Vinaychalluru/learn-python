# Chef is a very experienced and well-known cook. He has participated in many cooking competitions in the past — so many that he does not even remember them all.

# One of these competitions lasted for a certain number of days. The first day of the competition was day S of the week (i.e. Monday, Tuesday etc.) and the last day was day E of the week. Chef remembers that the duration of the competition (the number of days between the first and last day, inclusive) was between L days and R days inclusive. Is it possible to uniquely determine the exact duration of the competition? If so, what is this duration?

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains two space-separated strings S and E, followed by a space and two space-separated integers L and R.
# Output
# For each test case, print a single line containing:

# the string "impossible" if there is no duration consistent with all given information
# the string "many" if there is more than one possible duration
# one integer — the duration of the competition, if its duration is unique
# Constraints
# 1≤T≤10,000
# 1≤L≤R≤100
# S is one of the strings "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday" or "friday"
# E is one of the strings "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday" or "friday"
# Subtasks
# Subtask #1 (100 points): original constraints

# Example Input
# 3
# saturday sunday 2 4
# monday wednesday 1 20
# saturday sunday 3 5
# Example Output
# 2
# many
# impossible

# Solution

import traceback

testCases = []

def readTestCases():
    global testCases
    nbr_of_test_cases = int(input())
    # _ is the ThrowAway Variable here
    for _ in range(nbr_of_test_cases):
        testCases.append(input())

def calcDuration(testCases):
    for tc in testCases:
        tc = tc.split()
        S = weekdays[tc[0]]
        E = weekdays[tc[1]]
        L = int(tc[2])
        R = int(tc[3])
        diff = L + (E - S + 1 - L) % 7
        if diff > R :
            print("impossible")
        else :
            if R >= diff + 7 :
                print("many")
            else :
                print(diff)
            

# Main
try:
    weekdays = {
        "saturday" : 1,
        "sunday" : 2,
        "monday" : 3,
        "tuesday" : 4,
        "wednesday" : 5,
        "thursday" : 6,
        "friday" : 7
    }
    readTestCases()
    calcDuration(testCases)
except Exception as e:
    print("Exception Thrown - ", repr(e))
    traceback.print_exc()


# w = ['saturday', 'sunday', 'monday', 'tuesday',
#      'wednesday', 'thursday', 'friday']
# t = int(input())
# for _ in range(t):
#     s, e, l, r = input().split()
#     s, e = w.index(s), w.index(e)
#     l, r = int(l), int(r)
#     d = l + (e + 1 - s - l) % 7
#     if d > r:
#         print('impossible')
#     elif d + 7 <= r:
#         print('many')
#     else:
#         print(d)