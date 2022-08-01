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


# takes in the size of the font and returns the font for the game
def getFont(size):
    return pygame.font.Font('freesansbold.ttf', size)

# runs this function if only playing against CPU
def onePlayer():
    while True:
        # global mouse position
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # might add a follow up screen for hard vs easy buttons for player one
        SCREEN.fill(WHITE)

        PLAY_TEXT = getFont(45).render("This is the One Player.", True, BLACK)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 240))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(340, 340),
                           textInput="BACK", font=getFont(75),
                           baseColor=BLACK, hoveringColor=GREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# runs this function if playing PVP
def twoPlayer():
    ticTacToegame = TicTacToe(2)
    playersTurn = ticTacToegame.getRandomStart()
    while True:
        # global mouse position
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)
        

        if playersTurn == 0:
            PLAY_TEXT = getFont(25).render("It is Player Two's Turn:", True, BLACK)
        else:
            PLAY_TEXT = getFont(25).render("It is Player One's Turn:", True, BLACK)

        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 40))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        nextTurn = Button(image=None, pos=(340, 340),
                           textInput="Next Turn", font=getFont(75),
                           baseColor=BLACK, hoveringColor=GREEN)

        nextTurn.changeColor(PLAY_MOUSE_POS)
        nextTurn.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextTurn.checkForInput(PLAY_MOUSE_POS):
                    if playersTurn == 0:
                        playersTurn = 1
                    else:
                        playersTurn = 0
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getFont(100).render("TicTacToe:", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 100))

        ONE_PLAYER_BUTTON = Button(image=pygame.image.load("assets/Player_Rect.png"), pos=(320, 200), 
                            textInput="One Player", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White")
        TWO_PLAYER_BUTTON = Button(image=pygame.image.load("assets/Player_Rect.png"), pos=(320, 320), 
                            textInput="Two Player", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit_Rect.png"), pos=(320, 440), 
                            textInput="QUIT", font=getFont(50), baseColor="#d7fcd4", hoveringColor="White")

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
