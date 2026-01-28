from time import process_time
from datetime import timedelta

def decoratorFunction(innerFunction):
    def wrapper():
        start = process_time()
        innerFunction()
        end = process_time()
        return end - start
    return wrapper

@decoratorFunction
def addTwoNumbers():
    return 985138 + 461532

processTimeElapsed = addTwoNumbers()
print(timedelta(seconds=processTimeElapsed))
