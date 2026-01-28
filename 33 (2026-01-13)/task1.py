from curses.ascii import isdigit


def stringToList(userInput):
    if str(userInput).isdigit():
        raise TypeError("String cannot be a number")
    else:
        return userInput.split()