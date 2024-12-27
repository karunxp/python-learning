# ask a user for name
# Example Arun Kumar
# print count of each words
# output :
    #   A : 1 
    #   r : 2
    #   u : 2
    #   n : 1
    #   K : 1
    #   u : 2
    #   m : a
    #   a : 1
    #   r : 2

name = input("Enter your name : ")
i = 0
while i < len(name):
    #print(name[i]) 
    #print(name.count(name[i]))
    print(f"{name[i]} : {name.count(name[i])}") 
    i += 1

#####
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
    print(f"{name[i]} : {name.count(name[i])}") 
    i += 1

