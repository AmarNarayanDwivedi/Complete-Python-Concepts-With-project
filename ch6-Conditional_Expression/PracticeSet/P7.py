'''Write a program to find out whether a given post is talking about “Crypto” or not. 
'''

post = input(" Write your post :" )

if "crypto".lower() in post.lower() :
    print("The post is talking about 'Crypto'")

else :
    print("The post is not talking about 'Crypto'")

