# Name possibilities:
# 2: title, last; first, last; last, suffix;
# 3: title, first, last; first, middle, last; first, last, suffix;
# 4: title, first, middle, last; first, middle, last, suffix; title, first, last, suffix;
# 5: title, first, middle, last, suffix

def parse_full_name(full_name):
    nameDictionary = dict()
    nameList = full_name.split(' ')
    nameListLength = len(nameList)
    titles = ["Mr.", "Mrs.", "Ms.", "Miss", "Mx.", "Mstr.", "Dr.", "Prof.", "Judge", "Justice", "Coach", "Chef", "Rev.", "Father", "Fr.", "Pastor", "Rabbi", "Imam", "Sister", "Sr.", "Brother", "Br.", "Cantor", "Gen.", "Col.", "Maj.", "Capt.", "Lt.", "Sgt.", "Adm.", "The Honorable", "Hon.", "Ambassador", "President", "Senator", "Representative", "Sir", "Dame", "Lord", "Lady", "Duke", "Duchess", "His Excellency", "Her Excellency"]
    suffixes = ["Jr.", "Sr.", "II", "III", "IV", "V", "Esq.", "PhD", "MD", "JD", "DDS", "DVM", "EdD", "PsyD", "PharmD", "LLD", "DO", "DC", "RN", "BSN", "MSN", "NP", "PA", "PE", "CPA", "CFA", "PMP", "LCSW", "LPC", "CFP", "SHRM-CP", "LEED AP", "OBE", "MBE", "CBE", "KBE", "JP", "Ret.", "USA", "USN", "USAF", "USMC", "SJ", "OP", "OSB"]

    if nameListLength == 5:
        nameDictionary["title"] = nameList[0]
        nameDictionary["first"] = nameList[1]
        nameDictionary["middle"] = nameList[2]
        nameDictionary["last"] = nameList[3]
        nameDictionary["suffix"] = nameList[4]

    elif nameListLength == 4:
        if nameList[0] in titles and nameList[nameListLength-1] not in suffixes:
            nameDictionary["title"] = nameList[0]
            nameDictionary["first"] = nameList[1]
            nameDictionary["middle"] = nameList[2]
            nameDictionary["last"] = nameList[3]
            nameDictionary["suffix"] = nameList[3]
        elif nameList[0] in titles and nameList[nameListLength-1] in suffixes:
            nameDictionary["first"] = nameList[0]
            nameDictionary["middle"] = nameList[1]
            nameDictionary["last"] = nameList[2]
            nameDictionary["suffix"] = nameList[3]
        else:
            nameDictionary["title"] = nameList[0]
            nameDictionary["first"] = nameList[1]
            nameDictionary["last"] = nameList[2]
            nameDictionary["suffix"] = nameList[3]

    elif nameListLength == 3:
        if nameList[0] in titles:
            nameDictionary["title"] = nameList[0]
            nameDictionary["first"] = nameList[1]
            nameDictionary["last"] = nameList[2]
        elif nameList[nameListLength-1] not in suffixes:
            nameDictionary["first"] = nameList[0]
            nameDictionary["middle"] = nameList[1]
            nameDictionary["last"] = nameList[2]
        else:
            nameDictionary["first"] = nameList[0]
            nameDictionary["last"] = nameList[1]
            nameDictionary["suffix"] = nameList[2]

    else:
        if nameList[0] in titles:
            nameDictionary["title"] = nameList[0]
            nameDictionary["last"] = nameList[1]
        elif nameList[nameListLength-1] not in suffixes:
            nameDictionary["first"] = nameList[0]
            nameDictionary["last"] = nameList[1]
        else:
            nameDictionary["last"] = nameList[0]
            nameDictionary["suffix"] = nameList[1]

    return nameDictionary

# Possibilities:
# If title exists: title, last; title, first, last; title, first, middle, last; title, first, last, suffix; title, first, middle, last, suffix;
# If suffix exists (excluding forementioned examples): last, suffix; first, last, suffix; first, middle, last, suffix;
# If neither exists: first, last; first, middle, last;

def format_name_formal(name_dict):
    if "title" in name_dict:
        if "suffix" in name_dict:
            if "middle" in name_dict:
                return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()} {name_dict['middle'].capitalize()} {name_dict['suffix'].capitalize()}"
            else:
                return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()} {name_dict['suffix'].capitalize()}"
        elif "middle" in name_dict:
            return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()} {name_dict['middle'].capitalize()}"
        elif "first" in name_dict:
            return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()}"
        else:
            return f"{name_dict['last'].upper()}"
    elif "suffix" in name_dict:
        if "middle" in name_dict:
            return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()} {name_dict['middle'].capitalize()} {name_dict['suffix'].capitalize()}"
        elif "first" in name_dict:
            return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()} {name_dict['suffix'].capitalize()}"
        else:
            return f"{name_dict['last'].upper()}, {name_dict['suffix'].capitalize()}"
    else:
        if "middle" in name_dict:
            return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()} {name_dict['middle'].capitalize()}"
        else:
            return f"{name_dict['last'].upper()}, {name_dict['first'].capitalize()}"

test_name = "Dr. John Paul Smith Jr."
parsed = parse_full_name(test_name)
print(parsed)
print(format_name_formal(parsed))