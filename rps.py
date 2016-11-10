from random import randint
from sys import exit

players = [
		"rock",
		"paper",
		"scissors"
	]	
opponent = players[randint(0, 2)]
result = {
		1 : "Rock beats Scissors! You win!",
		2 : "Rock loses to Paper! You lost!",
		3 : "Scissors beats Paper! You win!", 
		4 : "Scissors loses to Rock! You lose!",
		5 : "Paper beats Rock! You win!",
		6 : "Paper loses to Scissors! You lose!", 
		7 : "It's a tie!"
	}

def game(opponent):
	print("\nWelcome to the battle of the century!")
	print("Choose your weapon:\n")
	print("Rock,")
	print("Paper,")
	print("or Scissors!")
	
	choice = raw_input("> ")
	
	if choice.lower() == "rock":
		if opponent == "scissors":
			print result[1]
			print("Wasn't that fun!?")
			return try_again()
		elif opponent == "paper":
			print result[2]
			print("Wasn't that fun!?")
			return try_again()
		else:
			print result[7]
			print("Wasn't that fun!?")
			return try_again()
	elif choice.lower() == "scissors":
		if opponent == "paper":
			print result[3]
			print("Wasn't that fun!?")
			return try_again()
		elif opponent == "rock":
			print result[4]
			print("Wasn't that fun!?")
			return try_again()
		else:
			print result[7]
			print("Wasn't that fun!?")
			return try_again()
	elif choice.lower() == "paper":
		if opponent == "rock":
			print result[5]
			print("Wasn't that fun!?")
			return try_again()
		elif opponent == "scissors":
			print result[6]
			print("Wasn't that fun!?")
			return try_again()
		else:
			print result[7]
			print("Wasn't that fun!?")
			return try_again()
	else:
		print("That is not an option. Please try again.")
		return try_again()
	
def try_again():
	print("Would you like to try again?")
	
	try_again = raw_input("> ")
	
	if try_again.lower() == "yes":
		opponent = players[randint(0,2)]
		return game(opponent)
	else:
		exit()
		
game(opponent)