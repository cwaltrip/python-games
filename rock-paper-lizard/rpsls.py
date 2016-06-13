# Rock, Paper, Scissors, Lizard, Spock

# Originally written for the Coursera/Rice University course
# 'An Introduction to Interactive Programming in Python (Part 1)'

import random

def name_to_number(name):
    # Convert name to number
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print("Illegal value for 'name'!")
    # Return the result
    return number

def number_to_name(number):
    # Convert number to a name
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print("Illegal value for 'number'!")
    # Return the result
    return name
    

def rpsls(player_choice): 
    # Print a blank line between rounds/games
    print("")
    # Ask for the player's choice
    print("Player chooses " + player_choice)
    player_number = name_to_number(player_choice)
    # Use random to determine computer's choice
    comp_number = random.randrange(4)
    comp_choice = number_to_name(comp_number)
    # Alert the user
    print("Computer chooses " + comp_choice)
    # Determine who wins
    result = (comp_number - player_number) % 5
    # Print the results of this round/game
    if (result == 1 or result == 2):
        print("Computer wins!")
    elif (result == 3 or result == 4):
        print("Player wins!")
    else:
        print("Player and computer tie!")
    
# Required tests
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

