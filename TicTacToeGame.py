
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

        # checks to see if cpu is moving first
        if self.moves == 1 and self.isBoardEmpty():
            openingMove = random.randint(0, 3)
            if openingMove == 0:
                self.setStringAtCoordinate('O', 0, 1)
            elif openingMove == 1:
                self.setStringAtCoordinate('O', 1, 0)
            elif openingMove == 2:
                self.setStringAtCoordinate('O', 1, 2)
            elif openingMove == 3:
                self.setStringAtCoordinate('O', 2, 1)

        # checks to see if cpu is moving second
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
                self.setStringAtCoordinate('O', 2, 1)
            elif self.getStringAtCoordinate(1, 0) == 'X':
                self.setStringAtCoordinate('O', 1, 2)
            elif self.getStringAtCoordinate(1, 2) == 'X':
                self.setStringAtCoordinate('O', 1, 0)
            elif self.getStringAtCoordinate(2, 1) == 'X':
                self.setStringAtCoordinate('O', 0, 1)
            else:
                self.setStringAtCoordinate('O', 1, 1)

        # checks to see if cpu is moved first
        elif self.moves == 3:
            # checks to see if the X in the middle
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
            # checks to see if the X in the top left
            elif self.getStringAtCoordinate(0, 0) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    self.setStringAtCoordinate('O', 1, 0)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    self.setStringAtCoordinate('O', 0, 1)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    self.setStringAtCoordinate('O', 2, 2)
            # checks to see if the X in the top middle
            elif self.getStringAtCoordinate(0, 1) == 'X':
                if self.getStringAtCoordinate(1, 0) == 'O':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    self.setStringAtCoordinate('O', 0, 2)
            # checks to see if the X in the top right
            elif self.getStringAtCoordinate(0, 2) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    self.setStringAtCoordinate('O', 1, 2)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    self.setStringAtCoordinate('O', 1, 0)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    self.setStringAtCoordinate('O', 0, 1)
            # checks to see if the X in the middle left
            elif self.getStringAtCoordinate(1, 0) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    self.setStringAtCoordinate('O', 2, 1)
            # checks to see if the X in the middle right
            elif self.getStringAtCoordinate(1, 2) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    self.setStringAtCoordinate('O', 2, 2)
            # checks to see if the X in the bottom left
            elif self.getStringAtCoordinate(2, 0) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    self.setStringAtCoordinate('O', 2, 1)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    self.setStringAtCoordinate('O', 1, 0)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    self.setStringAtCoordinate('O', 0, 2)
            # checks to see if the X in the bottom middle
            elif self.getStringAtCoordinate(2, 1) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    self.setStringAtCoordinate('O', 2, 2)
            # checks to see if the X in the bottom right
            elif self.getStringAtCoordinate(2, 2) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(2, 1) == 'O':
                    self.setStringAtCoordinate('O', 1, 2)
                elif self.getStringAtCoordinate(1, 2) == 'O':
                    self.setStringAtCoordinate('O', 2, 1)

        # checks to see if cpu is moved second
        elif self.moves == 4:
            # checks to see if x is in the middle and all possiblities
            if self.getStringAtCoordinate(1, 1) == 'X':
                if self.getStringAtCoordinate(0, 0) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(0, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 1)
                elif self.getStringAtCoordinate(0, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 0) == 'X':
                    self.setStringAtCoordinate('O', 1, 2)
                elif self.getStringAtCoordinate(1, 2) == 'X':
                    self.setStringAtCoordinate('O', 1, 0)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(2, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 1)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
            # checks to see if x is in the top left and all possiblities
            elif self.getStringAtCoordinate(0, 0) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(0, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 1)
                elif self.getStringAtCoordinate(1, 0) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 1, 0)
                elif self.getStringAtCoordinate(2, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 1, 0)
                elif self.getStringAtCoordinate(1, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 1)
            # checks to see if x is in the top middle and all possiblities
            elif self.getStringAtCoordinate(0, 1) == 'X':
                if self.getStringAtCoordinate(0, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(1, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(1, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 1, 2)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
            # checks to see if x is in the top right and all possiblities
            elif self.getStringAtCoordinate(0, 1) == 'X':
                if self.getStringAtCoordinate(1, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(1, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 1)
                elif self.getStringAtCoordinate(2, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 1, 2)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 1, 2)
            # checks to see if x is in the middle left and all possiblities
            elif self.getStringAtCoordinate(1, 0) == 'X':
                if self.getStringAtCoordinate(0, 0) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(0, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(0, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(2, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
            # checks to see if x is in the middle right and all possiblities
            elif self.getStringAtCoordinate(1, 2) == 'X':
                if self.getStringAtCoordinate(0, 0) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(0, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(1, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(2, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(2, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
            # checks to see if x is in the bottom left and all possiblities
            elif self.getStringAtCoordinate(2, 0) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(0, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 1)
                elif self.getStringAtCoordinate(1, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(2, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 1)
            # checks to see if x is in the bottom middle and all possiblities
            elif self.getStringAtCoordinate(2, 1) == 'X':
                if self.getStringAtCoordinate(0, 0) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(0, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 0) == 'X':
                    self.setStringAtCoordinate('O', 2, 2)
                elif self.getStringAtCoordinate(1, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 0)
                elif self.getStringAtCoordinate(1, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(2, 2) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
            # checks to see if x is in the bottom right and all possiblities
            elif self.getStringAtCoordinate(2, 2) == 'X':
                if self.getStringAtCoordinate(0, 0) == 'X':
                    self.setStringAtCoordinate('O', 0, 1)
                elif self.getStringAtCoordinate(0, 1) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(1, 0) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 2) == 'X':
                    self.setStringAtCoordinate('O', 0, 2)
                elif self.getStringAtCoordinate(2, 1) == 'X':
                    self.setStringAtCoordinate('O', 2, 0)

        # checks to see if cpu is moved first
        elif self.moves == 5:
            # checks to see if the X in the middle
            if self.getStringAtCoordinate(1, 1) == 'X':
                if self.getStringAtCoordinate(0, 1) == 'O':
                    if self.getStringAtCoordinate(1, 0) == 'O':
                        if self.getStringAtCoordinate(0, 0) != 'X':
                            self.setStringAtCoordinate('O', 0, 0)
                        elif self.getStringAtCoordiant(0, 0) == 'X':
                            self.setStringAtCoordinate('O', 2, 2)
                    elif self.getStringAtCoordinate(1, 2) == 'O':
                        if self.getStringAtCoordinate(0, 2) != 'X':
                            self.setStringAtCoordinate('O', 0, 2)
                        elif self.getStringAtCoordiant(0, 2) == 'X':
                            self.setStringAtCoordinate('O', 2, 0)
                elif self.getStringAtCoordinate(1, 0) == 'O':
                    if self.getStringAtCoordinate(0, 1) == 'O':
                        if self.getStringAtCoordinate(0, 0) != 'X':
                            self.setStringAtCoordinate('O', 0, 0)
                        elif self.getStringAtCoordiant(0, 0) == 'X':
                            self.setStringAtCoordinate('O', 2, 2)
                    elif self.getStringAtCoordinate(1, 2) == 'O':
                        if self.getStringAtCoordinate(2, 1) != 'X':
                            self.setStringAtCoordinate('O', 2, 0)
                        elif self.getStringAtCoordiant(2, 1) == 'X':
                            self.setStringAtCoordinate('O', 0, 2)
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
        
        
