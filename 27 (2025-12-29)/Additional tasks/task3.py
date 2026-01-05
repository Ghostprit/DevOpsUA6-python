def create_acronym(*args):

    acronym = ""
    formattedString = ""

    for arg in args:
        formattedString = arg.strip()
        acronym+=formattedString[0].upper()

    return acronym

print(create_acronym("Code", "Academy", "Lithuania"))
print(create_acronym("Hyper", "Text", "Markup", "Language"))