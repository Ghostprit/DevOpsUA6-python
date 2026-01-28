def decoratorOuterFunction(greeting):
    def decoratorFunction(splitString):
        def wrapper(*args, **kwargs):
            print("Before funtion execution: ", greeting)
            arr = splitString(*args, **kwargs)
            print("After function execution: ", greeting)
            return arr 
        return wrapper
    return decoratorFunction

@decoratorOuterFunction("Hello - this was passed")
def splitString(userString):
    words = userString.split()
    return words

print(splitString("Eurofighter Typhoon is a highly agile Air Superiority and Air-to-Surface, multi-role/swing-role weapon system."))