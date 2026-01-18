# super - function that used on child class to call a method or attributes from super class


class Shape():
    def __init__(self, color,filled):
        self.color = color
        self.filled = filled


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius= radius

    def describe(self):
        print(f'The value of this area is {3.14 * self.radius * self.radius} and is {'filled' if self.filled else "not filled"}')

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color,filled)
        self.width= width

    def describe(self):
        print(f'The value of this area is {self.width* self.width} and is {'filled' if self.filled else "not filled"}')


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color,filled)
        self.width= width
        self.height= height

    def describe(self):
        print(f'The value of this area is {self.width* self.height} and is {'filled' if self.filled else "not filled"}')


circle= Circle('Red', True, 8)
square= Square('Blue', False, 7)
triangle= Triangle('Yellow', True, 8,9)


triangle.describe()