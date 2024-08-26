#A class is a blueprint for creating object. 

#An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation. 

#CLASS ATTRIBUTES 
#An attribute that belongs to the class rather than a particular object. 
#Example: 

class Employee:
    company = " Microsoft"  # Specific to Each Class

p1 = Employee()  # Object Instatiation
print(p1.company)
Employee.company = "google"  # Changing Class Attribute
print(p1.company)

'''
INSTANCE ATTRIBUTES 
An attribute that belongs to the Instance (object). Assuming the class from the previous 

example: 
'''

class Students:
    sub = "maths"

Amar = Students()
Amar.sub = "English"

print(Amar.sub)