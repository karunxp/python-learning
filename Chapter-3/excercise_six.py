# MODIFY NUMBER GUESSING GAME

#import random
#winning_number = random.randint(1, 100)
#print(winning_number)
#number = input("Guess the number : ")
#number = int(number)

#if number == winning_number:
#    print("You WIN!!!")
#elif number < winning_number:
#    print("too low number")
#elif number > winning_number:
#    print("too high")

######
winning_number = 43
guess = 1
number = int(input("guess a number between 1 and 100"))
game_over = False

while not game_over:
    if number ==  winning_number:
        print(f"you win, and you this number in {guess} time")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
            guess += 1
            number = int(input("guess again : "))
        else:
            print("too high")
            guess += 1
            number = int(input("guess again : "))                    





######another way#######
import random
rnum = random.randint(1,100)
gnum = int(input("Guess a number: "))
i = 0
while True:
    if gnum == rnum:
        print(f"you win in {i} times")
        break
    else:
        if (gnum>rnum):
            print("too high")
        else:
            print("too low")
    i+=1
    gnum = int(input("Guess a number: "))

########
for i in range(1,101):
    number=int(input("0 to 100 guess any number: \n"))
    guess=13
    if number==guess:
        print(f"perfectly you win. and you total guess {i} times ")
        break
    elif number<guess:
        print("chose Too high number ")
    elif number>guess :
        print("chose Too low number ")