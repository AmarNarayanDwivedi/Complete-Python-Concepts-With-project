#Write a program to calculate the factorial of a given number using for loop

a = int(input("Enter a number : "))
if (a==0) or (a==1) :
    print("Factorial of 0 and 1 is 1")
else:
    fact = 1  # initialize factorial to 1
    i = 1
    while (i<=a):
        fact = fact * i
        i = i + 1

    print("Factorial of",a,"is",fact)