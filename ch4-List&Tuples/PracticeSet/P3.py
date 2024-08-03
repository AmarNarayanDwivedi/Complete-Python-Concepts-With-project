#  Check that a tuple type cannot be changed in python. 

a = (1, 2, 3, "amar")

a[1] = "am" # gives error 

print(a)