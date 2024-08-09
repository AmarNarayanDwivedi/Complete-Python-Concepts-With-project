#Write a program to print multiplication table of a given number using for loop. 
a = int(input("Enter a number : "))

i=int(1)
while i<int(11):
    b = int(i)*a
    print( a, " * " ,i ," = ", b)
    i+=1
