# practice for loop
# ask user a number like 1234565
# calculate sum of digits ----->  1+2+3+4+5+6

num=input("enter a number : ")
num_len=len(num)
i=0
total=0
for i in range(num_len):
    total+=int(num[i])
	
print(total)