def populatingUserInputList(length, targetValue):

    stringList = []
    targetValueIndex = 0
    targetFound = False

    for i in range(int(length)):
        stringList.append(input(f"Please enter list item #{i+1}: "))

    for i in range(len(stringList)):
        if stringList[i] == targetValue:
            targetFound = True
            targetValueIndex = i+1

    if targetFound == False:
        return -1

    return targetValueIndex

userInputListLength = input("Enter the length of the list: ")
userTargetValue = input("Enter the target value: ")

print(populatingUserInputList(userInputListLength, userTargetValue))