import re

def validate_password(password):

    # Creating boolean variables with a value of "False" for all the password checks
    lengthOK = False
    uppercaseOK = False
    lowercaseOK = False
    digitOK = False
    specialOK = False

    # Creating a list with most common characters allowed in passwords
    specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", "~", "`", "(", ")", "[", "]", "{", "}", "<", ">", ".", ",", ":", ";", "\"", "'", "?", "/", "\\", "|"]

    # Checking if the password length matches requirements
    # If satisfied - the "lengthOk" variable is given the value: True
    if len(password) >= 8:
        lengthOK = True

    # Checking each character inside the password and seeing if they satisfy any
    # or all of the requirements. If satisfied - the variable is given the value: True
    for character in password:
        if character.isupper():
            uppercaseOK = True
        if character.islower():
            lowercaseOK = True
        if character.isdigit():
            digitOK = True
        if character in specialCharacters:
            specialOK = True

    # Checking the state of boolean variables and displaying the matching message if the
    # requirements are satisfied or one of them is not
    if lengthOK:
        if uppercaseOK:
            if lowercaseOK:
                if digitOK:
                    if specialOK:
                        return (True, "Password is valid")
                    else:
                        return (False, "Password must contain a valid special character (!@#$%^&*-_+=~`()[]{}<>.,:;\"\'?/\\|)")
                else:
                    return (False, "Password must contain a digit")
            else:
                return (False, "Password must contain a lowercase character")
        else:
            return (False, "Password must contain an uppercase character")
    else:
        return (False, "Password must be at least 8 characters long")

print(validate_password("weak"))  # Expected: (False, "Password must be at least 8 characters long")
print(validate_password("StrongPass123!"))  # Expected: (True, "Password is valid")