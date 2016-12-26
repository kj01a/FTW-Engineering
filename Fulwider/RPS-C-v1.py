import random

#vars we gonna use 
options = ["rock","paper","scissor"]

#name = str(raw_input("What's your name?")
choice = raw_input("Choose your weapon   ")

##Just because
if choice == options [0] or options [1] or options [2]:
        print "good choice!"
else:
        print "That's not a weapon!"

enemy = random.choice (options)
print enemy

if choice == "rock":
        if enemy == "rock":
                print "Again slaves!"
        elif enemy == "paper":
                print "You Lose!"
        else:
                print "you win!"
elif choice == "paper":
        if enemy == "paper":
                print "Again slaves!"
        elif enemy == "scissor":
                print "You Lose!"
        else:
                print "you win! but you're a pussy for choosing paper"
elif choice == "scissor":
        if enemy == "scissor":
                print "Again slaves!"
        elif enemy == "rock":
                print "You Lose!"
        else:
                print "you win!"
