#write a recursive function to calculate the sum of first n natural numbers.

def sum(x):
    if x <= 0:
        return 0
    else :
        return x + sum(x-1)

n = int(input("Enter a number : "))
print("Sum of first", n, "natural numbers is", sum(n))