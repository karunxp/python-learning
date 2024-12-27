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
import random
#winning_number = 43
winning_number = random.randint(1, 100)
guess = 1
number = int(input("guess a number between 1 and 100 : "))
game_over = False

'''while not game_over:
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
'''

# DRY principle - don't repeat yourself 
####Best solutions ####
while not game_over:
    if number ==  winning_number:
        print(f"you win, and you this number in {guess} time")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
        else:
            print("too high")
        guess += 1
        number = int(input("guess again : ")) 

##Another way
'''
while True:
    if number ==  winning_number:
        print(f"you win, and you this number in {guess} time")
        break
    else:
        if number < winning_number:
            print("too low")
        else:
            print("too high")
        guess += 1
        number = int(input("guess again : ")) 
'''