# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random

# default values for the initial game
range = 100
tries = 0
limit = 7

# helper function to start/restart the game
def new_game():
    global secret_number
    global limit
    global tries
    # initialize global variables
    secret_number = random.randrange(0, range)
    if (range == 100):
        limit = 7
    elif (range == 1000):
        limit = 10
    tries = 0
    print("New game! I'm thinking of a number between 0 and " + str(range) + ".")
    print("Can you guess what it is? You have " + str(limit) + " guesses.")
    input_guess()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global range
    range = 1000
    new_game()
    
def print_guesses_remaining():
    guesses_remaining = limit - tries
    if (guesses_remaining > 1):
        print("You have " + str(guesses_remaining) + " guesses remaining.")
    else:
        print("You have only 1 guess left!")
    
def input_guess():
    global tries
    while (tries < limit):
		    tries += 1
		    guess = input('What is your guess?\n')
		    # print("Your guess is " + guess + ".")
		    if secret_number > int(guess):
		        print("Higher!")
		        print_guesses_remaining()
		    elif secret_number < int(guess):
		        print("Lower!")
		        print_guesses_remaining()
		    else:
		        print("That's correct!")
		        print("")
		        new_game()
    print("Sorry! You have run out of guesses.")
    print("The secret number was " + str(secret_number) + ".")
    new_game()
        
# create frame
# frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
# frame.add_button("Range is 0 to 100", range100, 200)
# frame.add_button("Range is 0 to 1000", range1000, 200)
# frame.add_input("Enter A Guess", input_guess, 200)

# call new_game 
new_game()
