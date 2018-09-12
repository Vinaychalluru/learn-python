# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.
# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).

import re

S = input('Enter the whole string S :')
k = input('Enter the search string k :')

# This will not capture the immediate duplicated values in a single string. Try search for 'aa' in 'aaadaa'
matchResults = list(re.finditer(k, S))
if matchResults:
    print(*[(matchObj.start(), matchObj.end()-1)
            for matchObj in matchResults], sep="\n", end="\n")
else:
    print("(-1, -1)")

# Another way using lookahead
matchResults = list(re.finditer(r'(?={})'.format(k), S))
if matchResults:
    print(*[(matchObj.start(), matchObj.start() + len(k) - 1)
            for matchObj in matchResults], sep="\n", end="\n")
else:
    print("(-1, -1)")

# Another way
pattern = re.compile(k)
r = pattern.search(S)
if not r:
    print("(-1, -1)")
else:
    while r:
        print("({0}, {1})".format(r.start(), r.end() - 1))
        r = pattern.search(S, r.start() + 1)
