
# EXERCISE, NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it. # Ask user to guess a number .
# if user guessed correctly then print "YOU WIN!!!!"
# if user didn't guessed correctly then :
# if user guessed lower than actual number then print "too low" # if user guessed higher than actual number then print "too high"
# google "how to generate random number in python " to generate random # winning number

winning_number = 27
guess_number = int(input("Guess the number between 1 and 100 : "))

#if int(winning_number) == int(guess_number):
#    print("You are Winner!!!")
#if int(winning_number) > int(guess_number):
#    print("too low number")
#if int(winning_number) < int(guess_number):
#    print("too high number")

if guess_number == winning_number:
    print("You are Winner!!!")
else: # nested if else
    if guess_number < winning_number:
        print("too low")
    else:
        print("too high")

### another method to create the program
if guess_number == winning_number:
    print("You are Winner!!!")
else:
    if guess_number < winning_number:
        print("too low")
    if guess_number > winning_number:
        print("too high")