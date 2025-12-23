# Declaring the list, containing 3 given student dictionaries

students = [
{
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 92, 88]
},
{
    "name": "Bob",
    "age": 22,
    "grades": [78, 82, 85, 80]
},
{
    "name": "Charlie",
    "age": 21,
    "grades": [95, 92, 98, 94, 96]
}
]

# Creating the index that will help with information formatting and finding a student by their average
number = 1
# Creating a dictionary that houses the index and calculated average of each student
avg = {}

# Printing an empty line to break up text in console
print("")

# Iterating through the created student dictionary:
# - Displaying the student name, age and grades
# - Calculating the average and populating the "avg" dictionary
# - Displaying the grade average
# - Updating the created index
# - Printing an empty line to break up the information in console

for student in students:
    print("Student "+str(number)+":")
    print("Name: "+student["name"])
    print("Age: "+str(student["age"]))
    print("Grades: "+str(student["grades"]))
    avg.update({number-1: sum(student["grades"]) / len(student["grades"])})
    print("Average: "+str(avg[number-1]))
    number += 1
    print("")

# Creating the variables for the highest average and student index
maxNum = 0
bestStudent = 0

# Iterating through "avg" dictionary and finding the highest average.
# In addition, saving the key-index of the student with the highest average
for key, value in avg.items():
    if value > maxNum:
        maxNum = value
        bestStudent = key

# Printing an empty line to break up text in console
print("")

# Displaying the top student (by average) name and their average following
# the given output example
print("Top student: "+students[bestStudent]["name"]+" with average "+str(avg[bestStudent]))