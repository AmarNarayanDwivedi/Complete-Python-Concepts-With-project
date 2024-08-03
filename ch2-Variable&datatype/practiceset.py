# 1. Write a python program to add two numbers. 

a = input("enter a number = ")
b = input("enter another number = ")

sum = int(a) + int(b)

 
print("sum of a and b is = ", sum)

# 2. Write a python program to find remainder when a number is divided by z. 

x = int(input("Enter a number = "))
z = int(input("Enter a divisor = "))

remainder = x % z

print("remainder when x is divided by z is = ", remainder)

# 3. Check the type of variable assigned using input () function. 

a = input("Enter a value = ")

print("Type of a is = ", type(a))

# 4. Write a python program to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80

a = int(input("Enter a number "))
b = int(input("Enter b number "))

print(" is a>b ",a>b)


 
# 5. Write a python program to find an average of two numbers entered by the user. 

a = float(input("Enter a number "))

b = float(input("Enter another number "))

average = (a + b) / 2

print("Average of a and b is = ", average)

# 6. Write a python program to calculate the square of a number entered by the user.

number = int(input("Enter a number "))

square = number * number

print("Square of the number is = ", square)
