#Write a program to find the greatest of four numbers entered by the user. 

a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
d = int(input("Enter a number  "))
e = int(input("Enter a number  "))
 
if (a>b) and (a>e) and (a>c) and (a>d):
    print("The greatest number is", a)

elif (b>a) and (b>e) and (b>c) and (b>d):
    print("The greatest number is", b)

elif (c>a) and (c>e) and (c>b) and (c>d):
    print("The greatest number is", c)

elif (d>a) and (d>e) and (d>b) and (d>c):
    print("The greatest number is", d)

else :
    print("The greatest number is", e)
