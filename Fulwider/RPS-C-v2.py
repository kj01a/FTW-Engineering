##Revising v1 to include functions 
import random

weapons = ["rock","paper","scissor"]
choice = ""

result = {
    1 : "Rock beats Scissors! You win!",
    2 : "Rock loses to Paper! You lost!",
    3 : "Scissors beats Paper! You win!", 
    4 : "Scissors loses to Rock! You lose!",
    5 : "Paper beats Rock! You win!",
    6 : "Paper loses to Scissors! You lose!", 
    7 : "It's a tie!"}
 
def weaponChoice(choice):	
    print """
    Welcome to Rock, Paper, Scissors!
    Be prepared for battle. First you
    shall choose a weapon for battle.
    Then the computer will choose and
    battle begins.

    Choose your weapon....
    """

    choice = raw_input("...")	

    if choice in weapons:
        return choice
    else:
        print "There is no weapon of that kind here. Try again."
        weaponChoice() 


def battle(choice):
    print choice
    enemy = random.choice(weapons)
    
    if choice.lower == "rock":
        if enemy == "rock":
            print "Again slaves!"
        elif enemy == "paper":
            print "You Lose!"
        else:
            print "you win!"

    elif choice.lower == "paper":
        if enemy == "paper":
            print "Again slaves!"
        elif enemy == "scissor":
            print "You Lose!"
        else:
            print "you win! but you're a pussy for choosing paper"

    elif choice.lower == "scissor":
        if enemy == "scissor":
            print "Again slaves!"
        elif enemy == "rock":
            print "You Lose!"
        else:
            print "you win!"
    else:
        print "error"


weaponChoice(choice)
battle(choice)
