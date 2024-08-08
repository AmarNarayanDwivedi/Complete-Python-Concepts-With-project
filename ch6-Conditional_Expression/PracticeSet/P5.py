#Write a program which finds out whether a given name is present in a list or not. 

names = ["John", "Jane", "Jack"]

name = input("Enter a name: ")

if name in names: 
    print(name, "is present in the list.")

else:
    print(name, "is not present in the list.")

