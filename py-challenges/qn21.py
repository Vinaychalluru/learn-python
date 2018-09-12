# Question 21
# Level 3

# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math


class Plane_point:
    'I am a point on a plane'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print('Destroying Plane_point instance %d %d' % (self.x, self.y))

    def __str__(self):
        return '%d %d' % (self.x, self.y)

    def __add__(self, other):
        return Plane_point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Plane_point(self.x - other.x, self.y - other.y)

    def getDistance(self):
        return round(math.sqrt(self.x**2 + self.y**2))


curr_pos = Plane_point(0, 0)

while True:
    inpStr = input('Enter a move detail : ')
    if not inpStr:
        break
    else:
        inpMove = inpStr.split(' ')
        direction = inpMove[0]
        steps = int(inpMove[1])
        if direction == 'UP':
            curr_pos = curr_pos + Plane_point(0, steps)
        elif direction == 'DOWN':
            curr_pos = curr_pos - Plane_point(0, steps)
        elif direction == 'LEFT':
            curr_pos = curr_pos - Plane_point(steps, 0)
        elif direction == 'RIGHT':
            curr_pos = curr_pos + Plane_point(steps, 0)
        else:
            print('Wrong direction ignored')

print('Distance from (0,0) is %d' % curr_pos.getDistance())

# Another way

pos = [0, 0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
