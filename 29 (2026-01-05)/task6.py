class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"I am {self.name} and I am {self.age} years old. I am an employee"

class manager(employee):

    def describe(self):
        return f"I am {self.name} and I am {self.age} years old. I am a manager"

    def manage(self):
        return  "The department is being managed"

class engineer(employee):
    def describe(self):
        return f"I am {self.name} and I am {self.age} years old. I am an engineer"

    def engineer(self):
        return "The project is being developed"

class intern(employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.time = 3

    def describe(self):
        return f"I am {self.name} and I am {self.age} years old. I am an intern"

    def endOfContract(self):
        return f"I will work for {self.time} more months"


managerObj = manager("John", 38)
engineerObj = engineer("James", 28)
internObj = intern("Bob", 18)

print(managerObj.describe())
print(managerObj.manage())
print("")
print(engineerObj.describe())
print(engineerObj.engineer())
print("")
print(internObj.describe())
print(internObj.endOfContract())

