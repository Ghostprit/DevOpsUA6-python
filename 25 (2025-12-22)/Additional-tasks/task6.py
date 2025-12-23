# Declaring the provided dictionary
book = {"title": "Python Crash Course", "author": "Eric Matthes", "year": "2019", "pages": 544, "available": True}

# Displaying the dictionary's information
print("Book Information:")
print("Title: " + book["title"])
print("Author: " + book["author"])
print("Year: " + book["year"])
print("Pages: " + str(book["pages"]))
print("Available: " + str(book["available"]))

# Printing an empty line to break up text in console
print("")

# Adding a new key
book["Genre"] = "programming"

# Changing the value of a key
book.update({"Available": False})

# Displaying the dictionary's keys
print("Keys: ", book.keys())

# Displaying the dictionary's values
print("Values: ", book.values())

# Printing an empty line to break up text in console
print("")

# Displaying the updated book dictionary
print("Updated Book:")
print(book)