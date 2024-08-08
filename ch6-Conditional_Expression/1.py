#IF ELSE AND ELIF IN PYTHON 

# Syntax: 
'''
if (condition1): # if condition1 is True 
print ("yes") 
elif(condition2): # if condition2 is True  
print("no") 
else:             
# otherwise 
print("maybe")  
'''   

#Example:

a = 9

if(a<5):
    print("a is less than 5")

else:
    print("a is greater than or equal to 5")

'''
IMPORTANT NOTES: 
1. There can be any number of elif statements. 
2. Last else is executed only if all the conditions inside elifs fail. 
'''