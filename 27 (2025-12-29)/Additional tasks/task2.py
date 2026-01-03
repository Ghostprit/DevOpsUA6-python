def create_email(first_name, last_name, domain="codeacademy.lt"):
    emailNameLastName = first_name.lower() + "." + last_name.lower() + "@"
    emailNameLastName = emailNameLastName.replace(" ", "")

    fullEmail = emailNameLastName + domain

    return fullEmail

print(create_email("John Paul", "Smith"))
print(create_email("Anna", "Doe", "gmail.com"))