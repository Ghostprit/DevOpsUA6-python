# Importing a library that makes splitting by special characters easier
import re

# A template function to format the string so as not the repeat identical code
def format_user_input(text):
    # Separating the user input string by spaces between words
    listOfStrings = text.split()

    # Iterating through separated strings and substituting special characters with nothing.
    # In addition - the string is converted to lowercase
    for i in range(len(listOfStrings)):
        listOfStrings[i] = re.sub('[^A-Za-z]', '', listOfStrings[i])
        listOfStrings[i] = listOfStrings[i].lower()

    return listOfStrings

def count_word_frequency(text):
    # Initializing the output dictionary and a list to be used in counting unique words
    frequencyStringDictionary = {}
    uniqueWords = []

    # Getting formatted list of strings from "format_user_input" function
    listOfStrings = format_user_input(text)

    # Converting "listOfStrings" as a set to eliminate strings that are not unique
    uniqueWords = set(listOfStrings)

    # Populating the "frequencyStringDictionary" with keys as the unique word
    # and the value as the number of string occurrence
    for word in uniqueWords:
        frequencyStringDictionary.update({str(word): listOfStrings.count(str(word))})

    return frequencyStringDictionary



def find_longest_words(text, n=3):
    # Initialising a list to store the output and a dictionary to store words and their lengths
    nLongestWords = []
    lengthStringDictionary = {}

    # Getting formatted list of strings from "format_user_input" function
    listOfStrings = format_user_input(text)

    # Populating the "lengthStringDictionary" with keys as the words themselves
    # and values as their lengths
    for string in listOfStrings:
        lengthStringDictionary.update({str(string): len(string)})

    # Sorting the "lengthStringDictionary" by its length values descending
    longestWords = sorted(lengthStringDictionary, key=lengthStringDictionary.get, reverse=True)

    # Populating the "nLongestWords" list, appending the first value given by the user or by a default value
    for i in range(n):
        nLongestWords.append(longestWords[i])

    return nLongestWords

def text_statistics(text, **kwargs):
    # Initializing the values to be used in calculating:
    # - Total words in a user provided string
    # - Total unique words in a user provided string
    # - Total length of alphabetic characters in a user provided string
    # - Total word length average in a user provided string
    totalWords = 0
    totalUniqueWords = 0
    totalWordLength = 0
    totalWordAverage = 0.0

    # Checking and assigning if the user has provided the values for
    # "show_frequency", "show_longest" and "top_n"
    showFrequency = kwargs.get('show_frequency', False)
    showLongest = kwargs.get('show_longest', False)
    topN = kwargs.get('top_n', 3)

    # Getting formatted list of strings from "format_user_input" function
    listOfStrings = format_user_input(text)

    # Adding the length of each word length to a shared value
    for i in range(len(listOfStrings)):
        totalWordLength += len(listOfStrings[i])

    # Setting values to variables:
    # - "totalWords" as the length of formatted user input string list
    # - "totalUniqueWords" as the length of a formatted user input string list converted to a set
    # - "totalWordAverage" as the total word character length divided by the amount of words
    totalWords = len(listOfStrings)
    totalUniqueWords = len(set(listOfStrings))
    totalWordAverage = totalWordLength / totalWords

    # Setting the base output that will be returned no matter what additional arguments user specifies
    results = (f"Total words: {totalWords}\n"
                f"Total unique words: {totalUniqueWords}\n"
                f"Average word length: {totalWordAverage:.2f}\n")

    # Returning information depending on the arguments the user specifies
    if showFrequency:
        if showLongest:
            return results + (f"Word frequency: {count_word_frequency(text)}\n"
                                f"Longest word: {find_longest_words(text)}\n")
        else:
            return results + f"Word frequency: {count_word_frequency(text)}\n"
    elif showLongest:
        return results + f"Longest word: {find_longest_words(text)}\n"
    else:
        return results