'''
A function is a group of statements performing a specific task. 
When a program gets bigger in size and its complexity grows, it gets difficult for a 
program to keep track on which piece of code is doing what! 
A function can be reused by the programmer in a given program any number of 
'''

#EXAMPLE AND SYNTAX OF A FUNCTION 
def fun1():
    print('hello')

#FUNCTION CALL
fun1()

'''
FUNCTIONS WITH ARGUMENTS 
A function can accept some value it can work with. We can put these values in the parentheses. 
'''
def greet (name):
    print(f"good moring {name}")

greet("Amar")

#DEFAULT PARAMETER VALUE
def greet2(name = "unknown"):
    print(f"good moring {name}")
greet2()

