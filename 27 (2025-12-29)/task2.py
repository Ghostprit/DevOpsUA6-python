def stringReversion(userInput):

    userInputList = []
    reversedListAsString = ""

    for character in userInput:
        userInputList.append(character)

    userInputLength = len(userInputList)

    for i in range(userInputLength):
        # "userInputList[userInputLength-i-1]" is disgusting, but it works
        reversedListAsString += userInputList[userInputLength-i-1]

    return reversedListAsString

print(stringReversion("Dassault Rafale"))
print(stringReversion("Eurofighter Typhoon"))
