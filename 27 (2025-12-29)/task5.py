def sortingStrings(listOfStrings):

    # Initializing lists to be used
    lengthStringList = []
    stringList = []

    # Populating "lengthStringList" with two values every index: length of string and the string itself
    for string in listOfStrings:
        lengthStringList.append((len(string), string))

    # Sorting "lengthStringList" by length first and alphabetically second
    lengthStringList.sort()

    # Populating "sortedList" only with string values
    for keyValue in lengthStringList:
        for key in keyValue:
            if isinstance(key, str):
                stringList.append(key)

    # Returning the string list with values sorted by their length first and alphabetically second
    return stringList

# Displaying the sorted strings by the provided string list
print(sortingStrings(["Ford", "Kia", "Peugeot", "Citroen", "Opel", "Plymouth", "Pagani"]))