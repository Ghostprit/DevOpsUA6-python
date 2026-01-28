import numpy

with open("numeric.csv", "r") as file:
    numbers = numpy.loadtxt(file, delimiter=",")
    print("Data from numeric.csv:")

mean = numpy.mean(numbers)
median = numpy.median(numbers)
mode = numpy.bincount(numbers.astype(int)).argmax()

print("Mean: "+str(mean))
print("Median: "+str(median))
print("Mode: "+str(mode))