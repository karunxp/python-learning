##
name, char = input("enter the values comma seperated ").split(",")

#print(name)
#print(char)

#print("Your name lenght is ", len(name))
#print("Charector count is ", name.count("k"))

print(f"length of your name: {len(name)}")
print(f"character count: {name.count(char)}") #case senstive

print(f"character count insenstive : {name.lower().count(char.lower())}") #case insenstive

#name.lower().count(char.lower())

####removing space and count the charactor
#name.strip().lower()
#char.strip().lower()

#name.strip().lower().count(char.strip().lower())

print(f"character count insenstive : {name.strip().lower().count(char.strip().lower())}") #case insenstive