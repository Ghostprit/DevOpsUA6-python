# Getting user inputs and assigning a variable type
name = (str(input("Please enter your name: ")))
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
likesProgramming = bool(input("Please enter whether you like programming (True/False): "))

# Printing an empty line to break up text in console
print("")

# Displaying user inputs
print("Name: ", name, type(name))
print("Age: ", age, type(age))
print("Height: ", height, type(height))
print("Likes: ", likesProgramming, type(likesProgramming))