# Getting the user input as a sentence
sentence = input("Please provide a sentence: ")

# Dividing the given sentence into individual words
listOfWords = sentence.split()

# Checking if the user input has at least 10 words. If not, error message is displayed
# and the script exits
if len(listOfWords) < 10:
    print("ERROR: Please provide a sentence with at least 10 words")
    exit()

# Initializing variables:
# - "listOfCharacters": holds all individual alphanumerical
#   characters of the provided sentence
# - "wordLengths": holds keys as words in the sentence and
#   values as length of the word
# - "iterationIndex": holds the value of a "for" cycle iteration
# - "maxLength": length of the longest word in the given sentence
# - "lengthIndex": holds the index of a word that is the longest
listOfCharacters = []
wordLengths = {}
iterationIndex = 0
maxLength = 0
lengthIndex = 0

# Iterating through the sentence by each character and populating
# "listOfCharacters" list by appending alphanumerical values
for character in sentence:
    if character.isalpha():
        listOfCharacters.append(character)

# Iterating through the individual words of the sentence and
# populating "wordLengths" dictionary by providing each word
# and its length as a key-value pair
# "maxLength" is updated every time a longer word is spotted
# "lengthIndex" receives a new word index every time a longer
# word is spotted
for word in listOfWords:
    wordLengths.update({word: len(word)})
    if len(word) > maxLength:
        maxLength = len(word)
        lengthIndex = iterationIndex
    iterationIndex += 1

# Printing an empty line to break up text in console
print("")

# Displaying the number of words and characters
print("Number of words: " + str(len(listOfWords)))
print("Number of characters: " + str(len(listOfCharacters)))

# Printing an empty line to break up text in console
print("")

# Displaying the word lengths
print("Word lengths: " + str(wordLengths))

# Printing an empty line to break up text in console
print("")

# Displaying the longest word by getting the key, using the
# "iterationIndex" variable
# Additionally, displaying the character length by simply
# using the "maxLength" variable
print("Longest word: "+list(wordLengths.keys())[list(wordLengths.values()).index(iterationIndex)]+" ("+str(maxLength)+" characters)")