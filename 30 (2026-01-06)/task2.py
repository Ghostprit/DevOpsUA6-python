def divideTwoNumbers(a, b):
    # Checking whether the provided values are correct
    try:
        result = int(a) / int(b)
    # Checking whether the provided values are zero
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    # Checking whether the provided values are integers
    except ValueError:
        return "Values must be integers"
    # If everything is correct - return the answer
    else:
        return result

print(divideTwoNumbers(1, 2))
print(divideTwoNumbers(1, 0))
print(divideTwoNumbers(1, "word"))