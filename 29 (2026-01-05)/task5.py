import math
from math import pi

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

rectObj = Rectangle(100, 200)
circleObj = Circle(100)

print(rectObj.area())
print(rectObj.perimeter())
print("")
print(circleObj.area())
print(circleObj.perimeter())