# Getting user inputs
name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
favProgrammingLanguage = str(input("Please enter your favorite programming language: "))

# Printing an empty line to break up text in console
print("")

# Displaying user inputs
print(str.upper(name))
print(str.lower(name))
print("Hello " + name + ", you love " + favProgrammingLanguage + "!")