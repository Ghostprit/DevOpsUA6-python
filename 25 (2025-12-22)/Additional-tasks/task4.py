# Declaring a list of favorite fruits
fruits = ["banana", "pineapple", "persimmon", "yuzu", "passion fruit"]

# Printing the original list
print("Original fruits: ", fruits)

# Adding an entry to the very end of the list
fruits.append("apple")
fruits.append("guava")

# Adding an entry at the very beginning of the list
fruits.insert(0, "mango")

# Displaying the list after adding the entries
print("After adding: ", fruits)

# Removing the fruit "yuzu"
fruits.remove("yuzu")

# Displaying the list after the removal
print("After removing yuzu: ", fruits)

# Sorting the list alphabetically
fruits.sort()

# Printing the list after sorting
print("Sorted list: ", fruits)

# Printing the total amount of fruit in the list
print("Total fruits: " + str(len(fruits)))