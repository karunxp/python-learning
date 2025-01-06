# function to check greatest number

def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(greatest(34,23,15))        

