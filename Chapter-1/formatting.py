#string formatting

name = "Arun_Kumar"
age = 36

print("hello " + name + " your age is " + str(age)) # wihout formatting # ugly syntex

#python3
print("hello {} your age is {}".format(name, age)) #with formatting

#python3.6
print(f"Hello {name} your age is {age}") #with formatting

print(f"Hello {name} your age is {age + 3}") #with formatting