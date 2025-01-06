
# Define is_palindrome function that take one word in string as input # and return True if it is palindrome else return False
# palindrome - word that reads same backwards as forwards
# example
# is_palindrome ("madam") -----> True
# is_palindrome ("naman") --- --> True
# is_palindrome ("horse") ------> False
# logic (algorithm)
# step 1 -> reverse the string
# step 2 -> compare reversed string with original string


# def is_palindrom(word):
#     reversed_word = word[::-1]
#     if word == reversed_word
#         return True
#     else:
#         return False
    
# another way
# 
# def is_palindrom(word):
#     if word ==  word[::-1]:
#         return True
#     return False    
    
print(is_palindrom("madam"))
print(is_palindrom("horse"))

