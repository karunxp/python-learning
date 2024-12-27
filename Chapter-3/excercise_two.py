
# EXERCISE - WATCH COCO
# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# Print 'you can watch coco movie'
# Else print 'sorry, you cannot watch coco'


user_name = input("Enter you name: ")
user_age = int(input("Enter you age:"))

if user_age >= 10 and (user_name[0] == 'a' or user_name[0] == 'A'):
    print("You can watch the coco movie")
else:
    print("sorry, you can't watch the movie")

