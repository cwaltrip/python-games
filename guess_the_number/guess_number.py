# Guess The Number

# Originally written for the Coursera/Rice University course
# 'An Introduction to Interactive Programming in Python (Part 1)'

import random

# Set default values
range = 100
tries = 0
limit = 7

# Function to start a new game
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
    
# Event handlers for control panel
def range100():
    # Button to change range to [0,100) and start a new game
    global range
    range = 100
    new_game()

def range1000():
    # Button to changes range to [0,1000) and start a new game 
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
        
# # Create SimpleGUI frame
# frame = simplegui.create_frame("Guess The Number", 200, 200)
# # Register event handlers and start frame
# frame.add_button("Range is 0 to 100", range100, 200)
# frame.add_button("Range is 0 to 1000", range1000, 200)
# frame.add_input("Enter A Guess", input_guess, 200)

# Start a game 
new_game()
