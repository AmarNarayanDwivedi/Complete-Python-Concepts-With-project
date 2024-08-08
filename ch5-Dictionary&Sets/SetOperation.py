# OPERATIONS ON SETS 
# Consider the following set:

s = {0,1,2,3,4,4,5,433,3,9,2,4,42,}

print(len(s)) # doesn't count repeated elements Output:8

# Updates the set s and removes 8 from s.
s.remove(4) # delete all 4 from set
print(s)

# Removes an arbitrary element from the set and return the element removed
print(s.pop())
print(s)

s2 = {9,99,999,9999,000,00,0}

#Returns a new set with all items from both sets.
print(s.union(s2))

#Return a set which contains only item in both sets
print(s.intersection(s2))

#Return a set which contains only item in first set but not in second set
print(s.difference(s2))

#Adds an element 22 to the set(s).
s.add(22)

#Remove an element 1 from the set(s). If the element is not present, discard() does nothing.
s.discard(1)

#Returns True if the set is a subset of another set.
s.issubset(s2)

#Returns True if the set is a superset of another set.
s.issuperset(s2)

#clear the set
s.clear()
