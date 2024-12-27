# excercise one of three
# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n

number = int(input("Enter any number to show the SUM : "))
#number = int(number)

total = 0
i = 1

while i <= number:
    total = total + i
    i = i + 1
print(total)
