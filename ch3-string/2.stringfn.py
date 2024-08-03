str  = "Amar Narayan Dwivedi"

# lenghth of string including space
print(len(str))  

# ALL in lower case
print(str.lower())

# ALL in upper case
print(str.upper())

# Aonly first letter will be capital 
print(str.capitalize())

# Count of a character in string
count = str.count("r")
print(count)

# Check if string ends with a specific character
print(str.endswith("i"))

# Check if string starts with a specific character
print(str.startswith("A"))

# Find index of a character in string
print(str.find("N"))

# Find index of a character in string
print(str.replace("Narayan", "Kumar"))