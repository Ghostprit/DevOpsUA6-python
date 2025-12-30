class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def calc_perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(100, 200)
print(rectangle1.calc_area())
print(rectangle1.calc_perimeter())

print()

rectangle2 = Rectangle(40, 3333)
print(rectangle2.calc_area())
print(rectangle2.calc_perimeter())