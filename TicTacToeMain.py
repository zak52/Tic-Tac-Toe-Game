import pygame, sys
from ButtonClass import Button
from TicTacToeGame import TicTacToe

pygame.init()

# Global Variables for pygame
WINDOWWIDTH = 640
WINDOWHEIGHT = 540
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Windown width is a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height is a multiole of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


# Color pallet:
#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE      = (  0,   0, 255)
LIGHTGRAY = (192, 192, 192)

# Sets the title of the window
pygame.display.set_caption("TicTacToeMenu")

# sets the background picture of the game
BG = pygame.image.load("assets/mainmenuBackground.jpg")
END_BG = pygame.image.load("assets/gameOverBackGround.jpeg")

# end game Screen
def endGame(winner):

    # runs the end game screen until either it switches back to menu or they quit the game
    while True:
        # sets the background of the screen with the end background picture
        SCREEN.blit(END_BG, (0, 0))

        END_GAME_MOUSE_POS = pygame.mouse.get_pos()

        # sees if the winner is player 1, 2 or if its a tie between the players
        if winner == 0:
            END_GAME_TEXT = getFont(75).render("Player One Won!!", True, "#b68f40")
        elif winner == 1:
            END_GAME_TEXT = getFont(75).render("Player Two Won!!", True, "#b68f40")
        elif winner == -1:
            END_GAME_TEXT = getFont(75).render("TIE GAME!!!", True, "#b68f40")

        # Creates a rectangle around the text the displays whos the winner
        END_RECT = END_GAME_TEXT.get_rect(center=(320, 100))

        # a button that allows the user to go back to the main menu
        PLAY_AGAIN_BUTTON = Button(image=pygame.image.load("assets/Player_Rect.png"), pos=(320, 300), 
                            textInput="PLAY AGAIN", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White", beenClicked=False)

        # Button allows them to quit the game
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit_Rect.png"), pos=(320, 440), 
                            textInput="QUIT", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White", beenClicked=False)

        # displays the winner to the screen 
        SCREEN.blit(END_GAME_TEXT, END_RECT)

        # displays both created buttons on the screen
        for button in [PLAY_AGAIN_BUTTON, QUIT_BUTTON]:
            button.changeColor(END_GAME_MOUSE_POS)
            button.update(SCREEN)

        # runs through the pygame to see what the user selects
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_AGAIN_BUTTON.checkForInput(END_GAME_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(END_GAME_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()
# takes in the size of the font and returns the font for the game
def getFont(size):
    return pygame.font.Font('freesansbold.ttf', size)

# runs this function if only playing against CPU
def onePlayer():
    # creates a tictactoe game with 1 players
    ticTacToegame = TicTacToe(1)
    # selects which user will go first
    playersTurn = ticTacToegame.getRandomStart()
    # creates the tictactoe board
    ticTacToegame.createBoard()

    # buttons to see if any of the buttons of the game board have been clicked
    TopLeftClicked = False
    TopMiddleClicked = False
    TopRightClicked = False
    MiddleLeftClicked = False
    MiddleClicked = False
    MiddleRightClicked = False
    BottomLeftClicked = False
    BottomMiddleClicked = False
    BottomRightClicked = False
    while True:
        # play mouse position
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # sets backgound color to white
        SCREEN.fill(WHITE)
        

        # displays who turn it is at the top of the screen
        if playersTurn == 0:
            PLAY_TEXT = getFont(25).render("It is Player One's Turn:", True, BLACK)
        else:
            PLAY_TEXT = getFont(25).render("It is CPU's Turn", True, BLACK)
            ticTacToegame.cpuTurn()
            if( ticTacToegame.getStringAtCoordinate(0,0) != '---'):
                TopLeftClicked = True
            elif( ticTacToegame.getStringAtCoordinate(0,1) != '---'):
                TopMiddleClicked = True
            elif( ticTacToegame.getStringAtCoordinate(0,2) != '---'):
                TopRightClicked = True
            elif( ticTacToegame.getStringAtCoordinate(1,0) != '---'):
                MiddleLeftClicked = True
            elif( ticTacToegame.getStringAtCoordinate(1,1) != '---'):
                MiddleClicked = True
            elif( ticTacToegame.getStringAtCoordinate(1,2) != '---'):
                MiddleRightClicked = True
            elif( ticTacToegame.getStringAtCoordinate(2,0) != '---'):
                BottomLeftClicked = True
            elif( ticTacToegame.getStringAtCoordinate(2,1) != '---'):
                BottomMiddleClicked = True
            elif( ticTacToegame.getStringAtCoordinate(2,2) != '---'):
                BottomRightClicked = True
            playersTurn = 0

        
        
            

        # displays the text of whos turn it is
        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 40))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # buttons for all of the board spaces on the tictactoe board
        TopLeft = Button(image=None, pos=(125, 120),
                           textInput=ticTacToegame.getStringAtCoordinate(0,0), font=getFont(75),
                           baseColor=BLACK, hoveringColor=GREEN, beenClicked=TopLeftClicked)
        
        TopMiddle = Button(image=None, pos=(300, 120),
                               textInput=ticTacToegame.getStringAtCoordinate(0,1), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=TopMiddleClicked)

        TopRight = Button(image=None, pos=(475, 120),
                               textInput=ticTacToegame.getStringAtCoordinate(0,2), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=TopRightClicked)

        MiddleLeft = Button(image=None, pos=(125, 250),
                               textInput=ticTacToegame.getStringAtCoordinate(1,0), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=MiddleLeftClicked)
            
        Middle = Button(image=None, pos=(300, 250),
                               textInput=ticTacToegame.getStringAtCoordinate(1,1), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=MiddleClicked)

        MiddleRight = Button(image=None, pos=(475, 250),
                               textInput=ticTacToegame.getStringAtCoordinate(1,2), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=MiddleRightClicked)

        BottomLeft = Button(image=None, pos=(125, 390),
                               textInput=ticTacToegame.getStringAtCoordinate(2,0), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=BottomLeftClicked)
            
        BottomMiddle = Button(image=None, pos=(300, 390),
                               textInput=ticTacToegame.getStringAtCoordinate(2,1), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=BottomMiddleClicked)

        BottomRight = Button(image=None, pos=(475, 390),
                               textInput=ticTacToegame.getStringAtCoordinate(2,2), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=BottomRightClicked)

        # draws the game board for tictactoe
        pygame.draw.line(SCREEN, BLACK, (400, 60), (400, 460), 4)
        pygame.draw.line(SCREEN, BLACK, (200, 60), (200, 460), 4)
        pygame.draw.line(SCREEN, BLACK, (75, 180), (525, 180), 4)
        pygame.draw.line(SCREEN, BLACK, (75, 320), (525, 320), 4)

        # displays all the buttons on the gameboard
        for button in [TopLeft, TopMiddle, TopRight, MiddleLeft, Middle, MiddleRight,
                       BottomLeft, BottomMiddle, BottomRight]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        # handles the user input for the tictactoe board
        for event in pygame.event.get():
            if ticTacToegame.isWin():
                endGame(winner = ticTacToegame.getWinner())
            elif ticTacToegame.isBoardFull():
                endGame(winner = ticTacToegame.getWinner())
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TopLeft.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        TopLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 0, 0 )
                        playersTurn = 1
                        ticTacToegame.incrementMoves()
                elif TopMiddle.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        TopMiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 0, 1 )
                        playersTurn = 1
                        ticTacToegame.incrementMoves()
                elif TopRight.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        TopRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 0, 2 )
                        playersTurn = 1
                        ticTacToegame.incrementMoves()
                elif Middle.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        MiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 1, 1 )
                        ticTacToegame.incrementMoves()
                elif MiddleRight.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        MiddleRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 1, 2 )
                        ticTacToegame.incrementMoves()
                elif MiddleLeft.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        MiddleLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 1, 0 )
                        ticTacToegame.incrementMoves()
                elif BottomMiddle.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        BottomMiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 2, 1 )
                        ticTacToegame.incrementMoves()
                elif BottomRight.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        BottomRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 2, 2 )
                        ticTacToegame.incrementMoves()
                elif BottomLeft.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        BottomLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 2, 0 )
                        ticTacToegame.incrementMoves()
                
        pygame.display.update()

# runs this function if playing PVP
def twoPlayer():
    # creates a tictactoe game with 2 players
    ticTacToegame = TicTacToe(2)
    # selects which user will go first
    playersTurn = ticTacToegame.getRandomStart()
    # creates the tictactoe board
    ticTacToegame.createBoard()

    # buttons to see if any of the buttons of the game board have been clicked
    TopLeftClicked = False
    TopMiddleClicked = False
    TopRightClicked = False
    MiddleLeftClicked = False
    MiddleClicked = False
    MiddleRightClicked = False
    BottomLeftClicked = False
    BottomMiddleClicked = False
    BottomRightClicked = False

    # runs the game for PVP
    while True:
        
        # play mouse position
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # sets backgound color to white
        SCREEN.fill(WHITE)
        

        # displays who turn it is at the top of the screen
        if playersTurn == 0:
            PLAY_TEXT = getFont(25).render("It is Player One's Turn:", True, BLACK)
        else:
            PLAY_TEXT = getFont(25).render("It is Player Two's Turn:", True, BLACK)

        # displays the text of whos turn it is
        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 40))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # buttons for all of the board spaces on the tictactoe board
        TopLeft = Button(image=None, pos=(125, 120),
                           textInput=ticTacToegame.getStringAtCoordinate(0,0), font=getFont(75),
                           baseColor=BLACK, hoveringColor=GREEN, beenClicked=TopLeftClicked)
        
        TopMiddle = Button(image=None, pos=(300, 120),
                               textInput=ticTacToegame.getStringAtCoordinate(0,1), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=TopMiddleClicked)

        TopRight = Button(image=None, pos=(475, 120),
                               textInput=ticTacToegame.getStringAtCoordinate(0,2), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=TopRightClicked)

        MiddleLeft = Button(image=None, pos=(125, 250),
                               textInput=ticTacToegame.getStringAtCoordinate(1,0), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=MiddleLeftClicked)
            
        Middle = Button(image=None, pos=(300, 250),
                               textInput=ticTacToegame.getStringAtCoordinate(1,1), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=MiddleClicked)

        MiddleRight = Button(image=None, pos=(475, 250),
                               textInput=ticTacToegame.getStringAtCoordinate(1,2), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=MiddleRightClicked)

        BottomLeft = Button(image=None, pos=(125, 390),
                               textInput=ticTacToegame.getStringAtCoordinate(2,0), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=BottomLeftClicked)
            
        BottomMiddle = Button(image=None, pos=(300, 390),
                               textInput=ticTacToegame.getStringAtCoordinate(2,1), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=BottomMiddleClicked)

        BottomRight = Button(image=None, pos=(475, 390),
                               textInput=ticTacToegame.getStringAtCoordinate(2,2), font=getFont(75),
                               baseColor=BLACK, hoveringColor=GREEN, beenClicked=BottomRightClicked)

        # draws the game board for tictactoe
        pygame.draw.line(SCREEN, BLACK, (400, 60), (400, 460), 4)
        pygame.draw.line(SCREEN, BLACK, (200, 60), (200, 460), 4)
        pygame.draw.line(SCREEN, BLACK, (75, 180), (525, 180), 4)
        pygame.draw.line(SCREEN, BLACK, (75, 320), (525, 320), 4)

        # displays all the buttons on the gameboard
        for button in [TopLeft, TopMiddle, TopRight, MiddleLeft, Middle, MiddleRight,
                       BottomLeft, BottomMiddle, BottomRight]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)
            
        # handles the user input for the tictactoe board
        for event in pygame.event.get():
            if ticTacToegame.isWin():
                endGame(winner = ticTacToegame.getWinner())
            elif ticTacToegame.isBoardFull():
                endGame(winner = ticTacToegame.getWinner())
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TopLeft.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        TopLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 0, 0 )
                        playersTurn = 1
                    else:
                        playersTurn = 0
                        TopLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 0, 0 )
                elif TopMiddle.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        TopMiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 0, 1 )
                        playersTurn = 1
                    else:
                        TopMiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 0, 1 )
                        playersTurn = 0
                elif TopRight.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        TopRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 0, 2 )
                        playersTurn = 1
                    else:
                        TopRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 0, 2 )
                        playersTurn = 0
                elif Middle.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        MiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 1, 1 )
                    else:
                        playersTurn = 0
                        MiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 1, 1 )
                elif MiddleRight.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        MiddleRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 1, 2 )
                    else:
                        playersTurn = 0
                        MiddleRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 1, 2 )
                elif MiddleLeft.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        MiddleLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 1, 0 )
                    else:
                        playersTurn = 0
                        MiddleLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 1, 0 )
                elif BottomMiddle.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        BottomMiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 2, 1 )
                    else:
                        playersTurn = 0
                        BottomMiddleClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 2, 1 )
                elif BottomRight.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        BottomRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 2, 2 )
                    else:
                        playersTurn = 0
                        BottomRightClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 2, 2 )
                elif BottomLeft.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                        BottomLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'X', 2, 0 )
                    else:
                        playersTurn = 0
                        BottomLeftClicked = True
                        ticTacToegame.setStringAtCoordinate( 'O', 2, 0 )
                
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getFont(100).render("TicTacToe:", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 100))

        ONE_PLAYER_BUTTON = Button(image=pygame.image.load("assets/Player_Rect.png"), pos=(320, 200), 
                            textInput="One Player", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White", beenClicked=False)
        TWO_PLAYER_BUTTON = Button(image=pygame.image.load("assets/Player_Rect.png"), pos=(320, 320), 
                            textInput="Two Player", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White", beenClicked=False)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit_Rect.png"), pos=(320, 440), 
                            textInput="QUIT", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White", beenClicked=False)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [ONE_PLAYER_BUTTON, TWO_PLAYER_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ONE_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    onePlayer()
                if TWO_PLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    twoPlayer()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



main_menu()
