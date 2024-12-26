# to remove the spaces from code output 
## method em hamesha "var.methodname" ka use hota hai
name = "          Arun         "
dots = "......................."

#print(name + dots)

print(name.lstrip() + dots)  # to remove left side space use lstrip() method
print(name.rstrip() + dots)  # to remove right side space use rstrip() method
print(name.strip() + dots)   # to remove both side space use strip() method

name2 = "       Arun       Kumar      "
print(name2.replace(" ","") + dots) # to remove all spaces between two words

#name.strip().lower()
#char.strip().lower()
#name.strip().lower().count(char.strip().lower())
