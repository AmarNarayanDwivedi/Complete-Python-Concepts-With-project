'''Write a program to find whether a given number is prime or not. '''

a = int(input("Enter a number: "))

if a <= 1:
    print("It is not a prime number")

else :
    i=2
    while i<a:
        if (a%i)==0:

             print("It is not a prime number")
             break
        i+=1
    else:
            print("It is a prime number")

              
