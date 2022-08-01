
import random

#global variables

NUM_PLAYERS = 0

class TicTacToe():

    def __init__(self, numOfPlayers):
        self.board = GAME_BOARD = []
        NUM_PLAYERS = numOfPlayers

    def createBoard(self):
        for i in range(3):
            row=[]
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def getRandomStart(self):
        return random.randint(0, 1)
