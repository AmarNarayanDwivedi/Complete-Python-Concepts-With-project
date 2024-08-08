#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams. 

comment = input("Comment : ")

a= "Make a lot of money"
b= "buy now" 
c= "subscribe this"
d= "click" 

if( a in comment) or ( b in comment) or ( c in comment) or ( d in comment) :
    print("Spam Detected")

else :
    print("Not Spam")