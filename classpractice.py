
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

Rectangle = Rectangle(12, 10)
print(Rectangle.rectangle_area())


