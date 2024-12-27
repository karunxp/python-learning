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
temp = ""
for x in range(len(name)):
    if name[x] not in temp:
        print(f"{name[x]} : {name.count(name[x])}")
        temp += name[x] 