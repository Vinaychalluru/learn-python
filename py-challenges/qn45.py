# Question 45

# 1 < n < 10^6
# 1 < h(i) < 100
# 1 < p(i) < 10^6

# There are n houses in the village in a straight road
# Each house in the village is numbered using two identifiers
# House No - h(i)
# Position No - p(i)
# Position p(i) can be related to the plot no. and thus it is unique for each house

# Find out the largest open land area available for building a house
# Output the house numbers in ascending order
# In case of more than one possibility, output the nearest house from the start of road

# 4
# 2 2
# 3 1
# 5 15
# 4 30

n = i = int(input())

houses = {}

while i > 0:
    house, pos = input().split(' ')
    house, pos = int(house), int(pos)

    houses[pos] = house
    i = i - 1

print(houses)

positions = sorted(houses.keys())
curr_area = max_area = 0
start_pos = 0
end_pos = 0

for i in range(1, len(positions)):
    curr_area = positions[i] - positions[i - 1]
    if curr_area > max_area:
        max_area = curr_area
        start_pos = positions[i - 1]
        end_pos = positions[i]
    
if houses[start_pos] < houses[end_pos]:
    print(houses[start_pos], houses[end_pos])
else:
    print(houses[end_pos], houses[start_pos])
