# Python lists are containers to store a set of values of any data type. 

    # Lists are defined using square brackets []. Elements in a list are separated by commas.

    # Lists are mutable, meaning you can change the elements of a list after it has been created.

    # Lists in Python support indexing and slicing. Indexing starts from 0. Negative indices start from -1.

#list indexing 
list1 = [7,9,"amar","abc",22]

print(list1[0])
print(list1[3])

# list methods

l1 =[1,2,8,9,6,8,7,3]
print(l1)

#sort list in ascending order
l1.sort()
print(l1)

#sort list in descending order
l1.reverse()
print(l1)

#add element to list at end of list
l1.append(2)
print(l1)

#insert element at specific index in list
l1.insert(222,2)
print(l1)

#remove element from list by index
l1.pop(3)
print(l1)

#remove element from list by value
l1.remove(1)
print(l1)