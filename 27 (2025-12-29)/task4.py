def printingArguments(numberOfUserArguments):

    listOfArguments = []

    for i in range(numberOfUserArguments):
        listOfArguments.append(input("Enter an argument: "))

    print("")

    for arg in listOfArguments:
        print(arg)


arguments = input("Enter the number of the amount of arguments you will provide: ")
print("")
printingArguments(int(arguments))