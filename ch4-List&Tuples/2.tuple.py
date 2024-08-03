# A tuple is an immutable data type in python.

# Syntax: (value1, value2, value3,...)

# Creating a tuple

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)

# Accessing elements of a tuple

print(my_tuple[0])  # Output: 1

print(my_tuple[2])  # Output: 3

# Slicing a tuple
print(my_tuple[1:3])  # Output: (2, 3)

# Concatenating tuples

tuple1 = (1, 2, 3)

tuple2 = (1,4, 5, 6)

concatenated_tuple = tuple1 + tuple2

print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#count(1) will return number of times 1 occurs in tuple
print(concatenated_tuple.count(1))  # Output: 2

#index(1) will return the first occurrence of 1 in tuple
print(concatenated_tuple.index(1))  # Output: 0
