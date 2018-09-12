# Question 40

# Question:
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

import math


class Circle:
    '''Class Circle'''

    def __init__(self, r):
        self.radius = r

    def __del__(self):
        pass

    def calcArea(self):
        return math.pi*self.radius**2


circleObj = Circle(10)

print('Area of the circleObj is ', circleObj.calcArea())
