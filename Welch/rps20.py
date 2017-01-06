#CHANGELOG
#Rewrote, made cleaner, need to comment whole thing...
#1.2 migrated to python 3.6
#2.0 changed to oo paradigm, and cleaned up the code.
#   Added more flavor text
#   Added comments

from random import randint
from sys import exit

class RockPaperScissors(object):
    def __init__(self):
        #Construct for player to chose from
        #Give options cardinal values for determining winner later.
        self.possilbe_warrior_choices = ["rock", "paper", "scissors"]
        self.warrior_ranks = {'rock' : 0, 'scissors' : 1, 'paper' : 2}

    def opponent_chooses_champion(self):
        #Assign random choice to computer player
        self.opponents_champion = self.possilbe_warrior_choices[randint(0, 2)]
        return self.opponents_champion

    def player_chooses_champion(self):
        #Player chooses their option
        self.players_champion = input("> ")
        print("\nAn excellent choice, Sire.") #Flava test
        #Catch if player is not choosing from available options.
        if self.players_champion.lower() in self.possilbe_warrior_choices:
            return self.players_champion
        else:
            #Flava text
            print("\nUnfortunarly, Sire, that champion was destroy in the last")
            print("RoShamBo. You will need to choose from the available warriors.")
            return self.player_chooses_champion()

    def rank_players_champion(self):
        #Assign value of player's choice to intger variable
        pc_rank = self.warrior_ranks[self.player_chooses_champion().lower()]
        return pc_rank

    def rank_opponents_champion(self):
        #Assign value of computer's choice to intger value
        npc_rank = self.warrior_ranks[self.opponent_chooses_champion()]
        return npc_rank

    def to_battle(self):
        #Compare integer variables to see who wins.
        pc = self.rank_players_champion()
        npc = self.rank_opponents_champion()

        print("\nAnd now... to battle! May the best champion win!")
        print("\nRO!")
        print("SHAM!")
        print("BOOOOOOOOOOOOO!!!") #Flava flav test
        print("\nYou have chosen:", self.players_champion, "as your champion.")
        print("\nAnd your opponent has chosen: ", self.opponents_champion, ".")

        if npc == pc:
            self.you_have_tied()
        elif (npc + 2) % 3 == pc:
            self.you_have_won()
        else:
            self.you_have_lost()

    def you_have_tied(self):
        print("\nThey are both vanquished, My Lord! It is a tie! A rare occurance,")
        print("My Lord, to be sure. But the RoShamBo must have a victor. Shall we")
        print("go again?")
        self.try_again()

    def you_have_won(self):
        #Choose this option for wine and women
        print("\nYou have won, My Lord! We shall return home to the rewards of wine")
        print("and women. Or shall we challenge our opposing Lord again?")
        self.try_again()

    def you_have_lost(self):
        #The most delicious flava text IMHO
        print("\nWe have lost, My Lord. It is a sad day, but the match was well met,")
        print("and both champions fought with naught but the highest honor. If")
        print("you wish, My Lord. You may challenge your opponent again, and")
        print("perhaps regain some modicum of glory. What say you?")
        self.try_again()

    def try_again(self):
        #Allow the player to quit when they choose
    	try_again = input("> ").lower()

    	if try_again == "yes":
            print("\n\n\n")
            self.welcome()
    	else:
    		exit()

    def welcome(self):
        #Starts game, starts flava text.
        print("\n\nWelcome, My Lord, to the RoShamBo. The games are about to begin.")
        print("\nThe rules are thus: You will choose from three warriors to be your")
        print("champion, and your opponent will do the same. And then they batte!")
        print("And to the victor go the spoils.")
        print("\nWe await your choice of champion. We have before you three")
        print("warriors with honor worthy fighting for you.")
        print("\nThe first is Rock. Strong and sturdy, this warrior will not budge")
        print("to any foe.")
        print("\nThe second warrior is Paper. Swift and nimble, she finishes her")
        print("opponents with precise strikes.")
        print("\nAnd last there is Scissors. His wit is sharp, My Lord. And his")
        print("blades sharper.")
        print("\nThe time has come, My Lord. Which warrior shall have the honor of")
        print("fighting as your champion?")
        self.to_battle()


game = RockPaperScissors() #Initializing...
game.welcome() #Onward to glory!
