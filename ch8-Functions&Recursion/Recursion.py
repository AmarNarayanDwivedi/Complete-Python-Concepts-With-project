'''
RECURSION 
Recursion is a function which calls itself. 
It is used to directly use a mathematical formula as function. 
'''

#factorial(n) = n x factorial (n-1)

def factorial(n):
    if n==0 or n==1:
        return 1
        
    else:
        return n*factorial(n-1)

print(factorial(5))


'''
factorial(5) returns 5 * factorial(4)
factorial(4) returns 4 * factorial(3)
factorial(3) returns 3 * factorial(2)
factorial(2) returns 2 * factorial(1)
factorial(1) returns 1 (base case)
'''