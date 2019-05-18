'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(object):

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius**2

    def circumf(self):
        return 2 * Circle.pi * self.radius


rec1 = Rectangle(2, 3)
print(rec1.area())
print(rec1.perimeter())

cir1 = Circle(2)
print(cir1.area())
print(cir1.circumf())
