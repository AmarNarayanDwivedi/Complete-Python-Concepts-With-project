a = {
    "key" : "value",
    "key2" : "Amar",
    "Amar" : "Narayan",
    "list" : [1,2,3,34]
}

# Returns a list of (key,value)tuples. 
print(a.items())

# Returns a list containing dictionary's keys
print(a.keys())



print(a.copy())
#Returns a shallow copy of the dictionary.



print(a.get("key", None))
#Returns the value for the specified key if the key is in the dictionary; otherwise, returns default.

print(a.items())
#Returns a view object that displays a list of a dictionary’s key-value tuple pairs.

print(a.keys())
#Returns a view object that displays a list of all the dictionary’s keys.

print(a.pop('key', None))
#Removes the specified key and returns the corresponding value. If the key is not found, it returns default.
print(a)

a.update({"abc":22})
print(a)
##Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.

print(a.values())
#Returns a view object that displays a list of all the dictionary’s values.

print(a.clear())
#Removes all items from the dictionary.


