# function one

def greater(a,b):
    if a > b:
        return a
    return b

#function two

def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
# final function
def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)
    #return greater(greater(a,b), c)  another way to compare

print(new_greatest(101,23,12))