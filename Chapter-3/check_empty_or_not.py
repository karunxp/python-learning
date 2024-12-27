# check empty or not
# important
name = "abc"
if name: # true is string is not empty
    print("string is not empty")
else:
    print("string is empty")

# another use case
name = input("enter your name : ")
if name:
    print(f"your name is {name}")
else:
    print("you did't enter anyting")