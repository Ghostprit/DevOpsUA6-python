# Declaring the list of giving numbers
numbers = [10, 25, 30, 45, 50, 60, 75, 80]

# Displaying all the numbers in the list
print("All numbers:")
for i in range(0, len(numbers)):
    print(numbers[i])

# Printing an empty line to break up text in console
print("")

# Displaying all the numbers greater than 40
print("Numbers greater than 40:")
for i in range(0, len(numbers)):
    if numbers[i] > 40:
        print(numbers[i])

# Printing an empty line to break up text in console
print("")

# Displaying the sum of the numbers in the list
print("Sum: " + str(sum(numbers)))

# Displaying the average of the numbers in the list
print("Average: " + str(sum(numbers) / len(numbers)))