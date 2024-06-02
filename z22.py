class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 4)
print("Area of the rectangle:", rectangle.compute_area())  