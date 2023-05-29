import math
import random

class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter=letter

        #we want all players to get their next move given a game
        def get_move(self,game):
            pass

class RandomComputerPlayer(Player):
    def __int__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.input mov(0-9):' )

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invlid Square. Try again.')
        return val