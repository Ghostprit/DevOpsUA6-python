sentence = input("Enter your sentence: ")
sentence = sentence.upper()
arr = {}

for char in sentence:
    if char not in arr:
        if char.isalpha():
            arr.update({char: 1})
    else:
        arr[char] += 1

for key, value in arr.items():
    print(key+": "+str(value))