##Revising v1 to include functions 
import random

weapons = ["rock","paper","scissor"]

result = {
    1 : "Rock beats Scissors! You win!",
    2 : "Rock loses to Paper! You lost!",
    3 : "Scissors beats Paper! You win!", 
    4 : "Scissors loses to Rock! You lose!",
    5 : "Paper beats Rock! You win!",
    6 : "Paper loses to Scissors! You lose!", 
    7 : "It's a tie!"}

##Welcome user and allow choice of weapon. Randomly 
def weaponChoice():	
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
        ##Add clearing the screen before reprinting 


##Generate CPU and Make comparison 
def battle():
    print "good so far"
    print choice



    

## Result printing 

weaponChoice()
battle()
print choice*5
