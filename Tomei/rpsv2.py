import random

weapons = ['rock', 'paper', 'scissors']

rock = 'rock'
scissors = 'scissors'
paper = 'paper'

dict = {rock:
"""
oh big tough guy choosing the rock.
Well you ain't fooling me ya panzy.
now go smash some skulls in.
""",
scissors:
"""
Damn it he got his hands on the scissors.
The dumbass is probably going to poke his own eyes out.
Well go run into some enemies and try not to decapitate yourself.
""",
paper:
"""
Heaven help us the little bugger chose the paper.
Get the medic ready!
Alright snowflake go dish out some papercuts.
"""
}

print "Welcome to the war maggot scum!"
print """
Unfortunately we don't have anymore
shiny weapons to waste on you.
We got a Rock, a pair of Scissors, and a piece of Paper.
Well what are you standing around for maggot.
Get out there and win some fights.
"""

player_one_choice = raw_input("Rock, Paper, or Scissors? ")

#if player_one_choice in weapons:# want it to check weapons list for correct weapons, having trouble.
if player_one_choice == 'rock':
	print dict[rock]# print flavor text
elif player_one_choice == 'scissors':
	print dict[scissors]
elif player_one_choice == 'paper':
	print dict[paper]
else:
	#while
	print "I told you maggot no shinies for you!"
	#Loop script that takes you back to the raw input

print """
You proceed ahead with your %s.
The battle feild is lit up by the explosions.
You are spotted by a monster!
""" % player_one_choice

monster = random.choice(weapons)

print "The monster has chossen %s prepare your ass!" % monster

if player_one_choice == 'rock':
	if monster == 'scissors':
		print "Some how you and your measely rock have found victory today!" 
	elif monster == 'paper':
		print "You are knocked unconcious and eviscerated on the battlefield."
	elif monster == 'rock':
		print "You and the monster are both morons using the same weapon against each other."
	else:
		print "You messed up kid, destroying the whole world."
elif player_one_choice == 'scissors':
	if monster == 'paper':
		print "Some how you and your measely scissors have found victory today!" 
	elif monster == 'rock':
		print "You are knocked unconcious and eviscerated on the battlefield."
	elif monster == 'scissors':
		print "You and the monster are both morons using the same weapon against each other."
	else:
		print "You messed up kid, destroying the whole world."
elif player_one_choice == 'paper':
	if monster == 'rock':
		print "Some how you and your measely paper have found victory today!" 
	elif monster == 'scissors':
		print "You are knocked unconcious and eviscerated on the battlefield."
	elif monster == 'paper':
		print "You and the monster are both morons using the same weapon against each other."
	else:
		print "You messed up kid, destroying the whole world."
	#loop script back to rawinput
else:
	print "You messed up kid, destroying the whole world."