#Added functions to the game.
#Would like to work on loops for better understanding

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

def intro():
	print "Welcome to the war maggot scum!"
	print """
	Unfortunately we don't have anymore
	shiny weapons to waste on you.
	We got a Rock, a pair of Scissors, and a piece of Paper.
	Well what are you standing around for maggot.
	Get out there and win some fights.
	"""

	player_one_choice = raw_input("Rock, Paper, or Scissors? ")#Determines players choice of Rock, paper, or scissors.

	if player_one_choice == 'rock':
		print dict[rock]# print flavor text
	elif player_one_choice == 'scissors':
		print dict[scissors]
	elif player_one_choice == 'paper':
		print dict[paper]
	else:
		print "I told you maggot no shinies for you!"

	print """
		You proceed ahead with your %s.
		The battle field is lit up by the explosions.
		You are spotted by a monster!
		""" % player_one_choice
		
	return player_one_choice#saves players choice of weapon to be recalled by other function

def victory(player_one_choice):
	monster = random.choice(weapons)#determines opponents choice of rock, paper, or scissors

	print "The monster has chosen %s prepare your ass!" % monster#Clarification
		
	if player_one_choice == 'rock':#Rock victory and loss tree
		if monster == 'scissors':
			print "Some how you and your measely rock have found victory today!" 
		elif monster == 'paper':
			print "You are knocked unconcious and eviscerated on the battlefield."
		elif monster == 'rock':
			print "You and the monster are both morons using the same weapon against each other."
		else:
			print "You messed up kid, destroying the whole world."
	elif player_one_choice == 'scissors':#Scissors victory and loss tree
		if monster == 'paper':
			print "Some how you and your measely scissors have found victory today!" 
		elif monster == 'rock':
			print "You are knocked unconcious and eviscerated on the battlefield."
		elif monster == 'scissors':
			print "You and the monster are both morons using the same weapon against each other."
		else:
			print "You messed up kid, destroying the whole world."
	elif player_one_choice	== 'paper':#paper victory and loss tree
		if monster == 'rock':
			print "Some how you and your measely paper have found victory today!" 
		elif monster == 'scissors':
			print "You are knocked unconcious and eviscerated on the battlefield."
		elif monster == 'paper':
			print "You and the monster are both morons using the same weapon against each other."
		else:
			print "You messed up kid, destroying the whole world."

	else:#for all other returns
		print "You messed up kid, destroying the whole world."

game = intro()
victory(game)
