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

print "Welcome to the war maggot scum!"
print """
Unfortunately we don't have anymore
shiny weapons to waste on you.
We got a Rock, a pair of Scissors, and a piece of Paper.
Well what are you standing around for maggot.
Get out there and win some fights.
"""

player_one_choice = raw_input("Rock, Paper, or Scissors? ")

if player_one_choice in weapons:# want it to check weapons list for correct weapons, having trouble.
	if weapons == 'rock':
		print dict[rock]# print flavor text
	elif weapons == 'scissors':
		print dict[scissors]
	elif weapons == 'paper':
		print dict[paper]
	else:
		print "I told you maggot no shinies for you!"
		#Loop script that takes you back to the raw input

print """
You proceed ahead with your %s.
The battle feild is lit up by the explosions.
You are spotted by a monster!
"""

monster = random.choice(weapons)

if player_one_choice > monster:
	print "Some how you and your measely %s have found victory today!" % player_one_choice
elif player_one_choice < monster:
	print "You are knocked unconcious and eviscerated on the battlefield."
elif player_one_choice == monster:
	print "You and the monster are both morons using the same weapon against each other."
	#loop script back to rawinput
else:
	print "You messed up kid, destroying the whole world."