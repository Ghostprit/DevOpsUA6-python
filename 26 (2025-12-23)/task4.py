count = input("Enter the amount of numbers you will be writing: ")
array = []
print("")

for i in range(int(count)):
    array.append(int(input("Enter the number: ")))

maxNum = array[0]
minNum = array[0]

print("")

for number in array:
    if number > maxNum:
        maxNum = number
    elif number < minNum:
        minNum = number

print("Largest number: ", maxNum)
print("Smallest number: ", minNum)