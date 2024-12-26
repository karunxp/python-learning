# replace() method
# find() method

string = "she is very beautiful and she is good actor"
#print(string.replace(" ", "_")) # replace all spaces " " with "_" 
#print(string.replace("is", "was")) # replace all "is" with "was" 

print(string.replace("is", "was", 1)) # replace only first "is" with "was"


string2 = "she is very beautiful and she is good actor"
#print(string2.find("is"))  # to find the string and character position
print(string2.find("is", 1))  # to find the string and character position by defining the start position

## find the word ir charactor position when you don't the current postion for string or charactor
is_pos1 = string2.find("is")  # is_pos1 ---> number
is_pos2 = string2.find("is", is_pos1 + 1)

print(is_pos2)


