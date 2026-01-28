def classDecorator(originalClass):
    numberOfTimes = {}
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.originalInstance = originalClass(*args, **kwargs)
            self.numberOfTimes = numberOfTimes
        
        def originalMethod(self):
            if 'originalMethod' not in numberOfTimes:
                numberOfTimes["originalMethod"] = 0
            numberOfTimes["originalMethod"] += 1
            return self.originalInstance.originalMethod()
            
    return Wrapper

@classDecorator
class originalClass:
    def originalMethod(self):
        return "This is a method."


obj = originalClass()
obj.originalMethod()
obj.originalMethod()
obj.originalMethod()
obj.originalMethod()
obj.originalMethod()
obj.originalMethod()
print(obj.numberOfTimes['originalMethod'])