
import random

#global variables



class TicTacToe():

    def __init__(self, numOfPlayers):
        self.board = GAME_BOARD = []
        self.numberOfPlayers = numOfPlayers
        self.winnerOfGame = -1
        self.moves = 0

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

                endGame = True
                winner = player
                for i in range(lengthOfBoard):
                    if self.board[i][lengthOfBoard - 1 - i] != playerInput:
                        endGame = False
                        winner = -1
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

    def isBoardEmpty(self):
        for row in self.board:
            for playerInput in row:
                if playerInput != '---':
                    return False
        return True
        
    def getWinner(self):
        return self.winnerOfGame

    def getNumberOfPlayers(self):
        return self.numOfPlayers

    def incrementMoves(self):
        self.moves +=1

    def cpuTurn(self):

        self.incrementMoves()

        if self.moves == 1 and self.isBoardEmpty():
            openingMove = random.randint(0, 7)
            if openingMove == 0:
                self.setStringAtCoordinate('O', 0, 0)
            elif openingMove == 1:
                self.setStringAtCoordinate('O', 0, 2)
            elif openingMove == 2:
                self.setStringAtCoordinate('O', 2, 0)
            elif openingMove == 3:
                self.setStringAtCoordinate('O', 2, 2)
            elif openingMove == 4:
                self.setStringAtCoordinate('O', 0, 1)
            elif openingMove == 5:
                self.setStringAtCoordinate('O', 1, 0)
            elif openingMove == 6:
                self.setStringAtCoordinate('O', 1, 2)
            elif openingMove == 7:
                self.setStringAtCoordinate('O', 2, 1)
                

        elif self.moves == 2:
            if self.getStringAtCoordinate(1, 1) == 'X':
                cpuMove = random.randint(0, 3)
                if cpuMove == 0:
                    self.setStringAtCoordinate('O', 0, 0)
                elif cpuMove == 1:
                    self.setStringAtCoordinate('O', 0, 2)
                elif cpuMove == 2:
                    self.setStringAtCoordinate('O', 2, 0)
                elif cpuMove == 3:
                    self.setStringAtCoordinate('O', 2, 2)
                    
            elif self.getStringAtCoordinate(0, 1) == 'X':
                cpuMove = random.randint(0,1)
                if cpuMove == 0:
                    self.setStringAtCoordinate('O', 0, 0)
                elif cpuMove == 0:
                    self.setStringAtCoordinate('O', 0, 2)
            elif self.getStringAtCoordinate(1, 0) == 'X':
                cpuMove = random.randint(0,1)
                if cpuMove == 0:
                    self.setStringAtCoordinate('O', 0, 0)
                elif cpuMove == 1:
                    self.setStringAtCoordinate('O', 2, 0)
            elif self.getStringAtCoordinate(1, 2) == 'X':
                cpuMove = random.randint(0,1)
                if cpuMove == 0:
                    self.setStringAtCoordinate('O', 0, 2)
                elif cpuMove == 1:
                    self.setStringAtCoordinate('O', 2, 2)
            elif self.getStringAtCoordinate(2, 1) == 'X':
                cpuMove = random.randint(0,1)
                if cpuMove == 0:
                    self.setStringAtCoordinate('O', 2, 0)
                elif cpuMove == 1:
                    self.setStringAtCoordinate('O', 2, 2)
            else:
                self.getStringAtCoordinate('O', 1, 1)

        elif self.moves == 3:
            if self.getStringAtCoordinate(1, 1) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    cpuMove = random.randint(0,1)
                    if cpuMove == 0:
                        self.setStringAtCoordinate('O', 1, 0)
                    elif cpuMove == 0:
                        self.setStringAtCoordinate('O', 1, 2)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    cpuMove = random.randint(0,1)
                    if cpuMove == 0:
                        self.setStringAtCoordinate('O', 0, 1)
                    elif cpuMove == 0:
                        self.setStringAtCoordinate('O', 2, 1)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    cpuMove = random.randint(0,1)
                    if cpuMove == 0:
                        self.setStringAtCoordinate('O', 1, 0)
                    elif cpuMove == 0:
                        self.setStringAtCoordinate('O', 1, 2)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    cpuMove = random.randint(0,1)
                    if cpuMove == 0:
                        self.setStringAtCoordinate('O', 2, 1)
                    elif cpuMove == 0:
                        self.setStringAtCoordinate('O', 0, 1)
                        
        return True
        
        
