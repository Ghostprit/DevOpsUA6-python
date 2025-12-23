operation = input("Enter the calculation operation you want to perform: (+,-,*,/,%): ")
firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))

print("")
if operation == "+":
    print(str(firstNum)+" + "+str(secondNum)+" = "+str(firstNum+secondNum))
elif operation == "-":
    print(str(firstNum)+" - "+str(secondNum)+" = "+str(firstNum-secondNum))
elif operation == "*":
    print(str(firstNum)+" * "+str(secondNum)+" = "+str(firstNum*secondNum))
elif operation == "/":
    print(str(firstNum)+" / "+str(secondNum)+" = "+str(firstNum/secondNum))
elif operation == "%":
    print(str(firstNum)+" % "+str(secondNum)+" = "+str(firstNum%secondNum))
else:
    print("ERROR: Please enter a valid operation")
