class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def setName(self, value):
        self.__name = value

    def setAge(self, value):
        self.__age = value

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

nameSet = "John"
ageSet = "19"
personObj = Person()
personObj.setName(nameSet)
personObj.setAge(ageSet)
print(personObj.getName())
print(personObj.getAge())
