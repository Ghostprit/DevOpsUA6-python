class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

    def __repr__(self):
        return f"Brand: {self.brand!r}, Model: {self.model!r}, Year: {self.year!r}"

car1 = Car("Ford", "Mustang", "2005")
print(car1.__str__())
print(car1.__repr__())

print()

car2 = Car("Peugeot", "205", "1983")
print(car2.__str__())
print(car2.__repr__())