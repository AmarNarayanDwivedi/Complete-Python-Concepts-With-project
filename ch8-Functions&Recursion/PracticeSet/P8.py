#Write a python function to print multiplication table of a given number. 

def printtabel(n,m=1):
    if m > 10:
        return 
    else:
        print( f"{n} * {m} = {n*m}")
    printtabel(n,m+1)

printtabel(5,1)
    