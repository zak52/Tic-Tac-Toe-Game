
import random

#global variables

NUM_PLAYERS = 0


class TicTacToe():

    def __init__(self, numOfPlayers):
        self.board = GAME_BOARD = []
        NUM_PLAYERS = numOfPlayers
        self.winnerOfGame = -1

    def createBoard(self):
        for i in range(3):
            row=[]
            for j in range(3):
                row.append('---')
            self.board.append(row)

    def getRandomStart(self):
        return random.randint(0, 1)

    def getStringAtCoordinate(self, row, col):
        return self.board[row][col]

    def setStringAtCoordinate(self, inputText, row, col):
        self.board[row][col] = inputText

    def isWin(self):
        # initalize variables
        winner = -1
        endGame = False

        players = [0, 1]

        lengthOfBoard = len(self.board)
        
        for player in players:
            if player == 0:
                playerInput = 'X'
            elif player == 1:
                playerInput = 'O'
                
            for i in range(lengthOfBoard):
                winner = player
                endGame = True
                for j in range(lengthOfBoard):
                    if self.board[i][j] != playerInput:
                        winner = -1
                        endGame = False
                        break

                if endGame:
                    self.winnerOfGame = winner
                    return endGame

            for i in range(lengthOfBoard):
                winner = player
                endGame = True
                for j in range(lengthOfBoard):
                    if self.board[j][i] != playerInput:
                        winner = -1
                        endGame = False
                        break

                if endGame:
                    self.winnerOfGame = winner
                    return endGame

                endGame = True
                winner = player
                for i in range(lengthOfBoard):
                    if self.board[i][i] != playerInput:
                        winner = -1
                        endGame = False
                        break
                if endGame:
                    print (winner)
                    self.winnerOfGame = winner
                    return endGame

        self.winnerOfGame = winner
        return endGame

        
    def isBoardFull(self):
        for row in self.board:
            for playerInput in row:
                if playerInput == '---':
                    return False
        return True

    def getWinner(self):
        return self.winnerOfGame
        
