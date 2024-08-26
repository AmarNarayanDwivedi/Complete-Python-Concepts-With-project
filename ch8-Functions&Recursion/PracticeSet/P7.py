# Write a python function to remove a given word from a list ad strip it at the same time. 

def srtriper(l , word):
    n = []
    for item in l :
        if not (item == word):
            n.append(item.strip(word)) 
    print(n)

l = ["heel", " us", "use", "user"]
srtriper(l,"us")