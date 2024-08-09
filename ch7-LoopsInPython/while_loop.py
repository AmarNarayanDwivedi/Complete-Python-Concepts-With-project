'''there are two types of loops in python. 
• while loops 
• for loops '''


#WHILE LOOP 
#Syntax:
#while (condition): 
# # The block keeps executing until the condition is true 
#Body of the loop 

#Example: Print numbers from 0 to 9

i= 0
while(i<10):
    print(i)
    i += 1 # increment i by 1

#Note:  If the condition never become false, the loop keeps getting executed.

#Write a program to print the content of a list using while loops.

my_list = ["a" , "b" , "c" , "d" , "e"]
j=0
while j<len(my_list):
    print(my_list[j])
    j += 1


