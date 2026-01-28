class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def grade(self):
        return 9


personObj = Person("John", 18)
studentObj = Student("Michael", 17)

print(personObj.name)
print(personObj.age)
print("")
print(studentObj.name)
print(studentObj.age)
print("")
print(studentObj.grade())