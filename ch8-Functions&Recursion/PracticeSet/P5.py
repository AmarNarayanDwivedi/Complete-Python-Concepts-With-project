# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3

def printpattern (n):
    if n <= 0:
        return 
    else:
        print("*" * n)
        printpattern(n-1)

print(printpattern(3))