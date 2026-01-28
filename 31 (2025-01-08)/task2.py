def fileIO(inputFile):
    lineCount = 0
    reader = open(inputFile, 'r')

    for line in reader:
        lineCount += 1

    reader.close()
    
    return lineCount

print(fileIO("input.txt"))