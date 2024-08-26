#SELF PARAMETER 

class Student: 
    sub = "maths"
    def standard(self):
        print(" not given yet ")

Amar = Student()
Amar.standard()

'''
STATIC METHOD 
Sometimes we need a function that does not use the self-parameter. We can define a static method like this:
'''

class Student:
    @staticmethod
    def greet():
        print("good morning teacher")

Abhay = Student()

Abhay.greet()

'''
__INIT__() CONSTRUCTOR 
__init__() is a special method which is first run as soon as the object is created. 

__init__() method is also known as constructor. 

It takes ‘self’ argument and can also take further arguments.
'''

class teacher:
    def __init__(self, name , sub):
        self.name = name
        self.sub = sub

royal = teacher("haroon", "maths")

print(royal.name)

