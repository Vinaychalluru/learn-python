# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array arr[] of n integers each separated by a space.

# Constraints
# 2 <= n <= 10
# -100 <= arr[i] <= 100

# Output Format
# Print the runner-up score.

n = int(input())
# arr = map(int, input().split()) # dropped from python ?
arr = input().split() # Note that this doesn't limit input to n items
uniqArr = list(set(arr))
uniqArr.sort()
print(uniqArr[-2])
