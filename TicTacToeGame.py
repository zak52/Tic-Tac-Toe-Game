
import random

#global variables
PLAYER_ONE_CHAR = 'X'
CPU_CHAR = 'O'



class TicTacToe():

    def __init__(self, numOfPlayers):
        self.board = GAME_BOARD = []
        self.numberOfPlayers = numOfPlayers
        self.winnerOfGame = -1
        self.moves = 0
        self.cpuBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8]

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

    def getBoard(self):
        return self.board


    """
    0 | 1 | 2
    _________
    3 | 4 | 5
    _________
    6 | 7 | 8

    """
    def setStringAtCoordinate(self, inputText, row, col):
        self.board[row][col] = inputText
        if row == 0:
            self.cpuBoard[col] = inputText
        elif row == 1:
            self.cpuBoard[col+3] = inputText
        elif row == 2:
            self.cpuBoard[col+6] = inputText
        

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

    def getMove(self):
        return self.moves


    def cpuTurn(self, board, player, depth):
        #if current state is at end of game
        if self.isWin():
            if self.winnerOfGame == 0:
                return 10  - depth    
            elif self.winnerOfGame == 1:
                return -10 + depth
            elif isBoardFull():
                return 0

        

        lengthOfBoard = len(self.board)
        
        # checks to see if were maximizing the players moves
        if player == 0:
            bestScore = -1000

            # goes through all possible moves on board
            for i in range(lengthOfBoard):
                for j in range(lengthOfBoard):

                    # checks for available moves
                    if board[i][j] == '---':

                       
                        board[i][j] = PLAYER_ONE_CHAR

                        bestScore = max( bestScore, self.cpuTurn( board, player + 1, depth+1))

                        board[i][j] = '---'

            return bestScore

        else:
            bestScore = 1000

             # goes through all possible moves on board
            for i in range(lengthOfBoard):
                for j in range(lengthOfBoard):

                     # checks for available moves
                    if board[i][j] == '---':

                        board[i][j] = CPU_CHAR

                        bestScore = min( bestScore, self.cpuTurn( board, player - 1, depth+1))

                        board[i][j] = '---'

            return bestScore

    def findBestMove(self):
        bestScore = 1000
        bestPossibleMove = (-1, -1)

        lengthOfBoard = len(self.board)
         # goes through all possible moves on board
        for i in range(lengthOfBoard):
            for j in range(lengthOfBoard):
                
                if self.board[i][j] == '---':
                    self.board[i][j] = CPU_CHAR

                    moveValue = self.cpuTurn(self.board, 0, 0)

                    self.board[i][j] = '---'

                    print(moveValue)
                    if moveValue < bestScore:
                        bestPossibleMove = (i , j)
                        bestScore = moveValue

        return bestPossibleMove

    def chooseRandomMove(self):
        move = [random.randint(0, 2), random.randint(0, 2)]
        return move
                        
        
