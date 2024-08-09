'''FOR LOOP 
A for loop is used to iterate through a sequence like list, tuple, or string [iterables]'''

#Syntax:

l = [1, 7, 8] 
for item in l: 
    print(item)
     # prints 1, 7 and 8     

'''RANGE FUNCTION IN PYTHON 

The range() function in python is used to generate a sequence of number. 
We can also specify the start, stop and step-size as follows: 
range(start, stop, step_size) 
# step_size is usually not used with range()'''

'''AN EXAMPLE DEMONSTRATING RANGE () FUNCTION. 

for i in range(0,7): # range(7) can also be used. 
print(i) # prints 0 to 6'''

'''THE BREAK STATEMENT 
‘break’ is used to come out of the loop when encountered. It instructs the program to – 
exit the loop now.'''

#Example: 
for i in range (0,80): 
    print(i)     
# this will print 0,1,2 and 3 
    if (i==3):
        break

'''THE CONTINUE STATEMENT 
‘continue’ is used to stop the current iteration of the loop and continue with the next 
one. It instructs the Program to “skip this iteration”.''' 

#Example: 

for i in range (0,80): 
    if (i%2 == 0):
        continue
    print(i) 

# this will print 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79