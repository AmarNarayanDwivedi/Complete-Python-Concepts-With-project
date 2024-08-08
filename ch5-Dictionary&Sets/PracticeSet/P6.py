'''
Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. 
''' 

dic = {}
name = input("enter your name ")
lang= input("enter your favorite language ")
dic.update({name : lang})
name = input("enter your name ")
lang= input("enter your favorite language ")
dic.update({name : lang})
name = input("enter your name ")
lang= input("enter your favorite language ")
dic.update({name : lang})
name = input("enter your name ")
lang= input("enter your favorite language ")
dic.update({name : lang})

print(dic)