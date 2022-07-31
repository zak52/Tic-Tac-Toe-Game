# TicTacToe 
# By Zach Kaufman exzachtlylast@gmail.com

import random, pygame, sys
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Windown width is a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height is a multiole of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

# Color pallet:
#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE      = (  0,   0, 255)
BGCOLOR = BLACK

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT # global variables for screen size
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('TicTacToe')

    setUpGameScreen()
    # showStartScreen()
    while True: # main games loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def setUpGameScreen():
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, BLACK, (400, 40), (400, 440), 4)
    pygame.draw.line(DISPLAYSURF, BLACK, (200, 40), (200, 440), 4)
    pygame.draw.line(DISPLAYSURF, BLACK, (75, 160), (525, 160), 4)
    pygame.draw.line(DISPLAYSURF, BLACK, (75, 320), (525, 320), 4)

    # pixObj = pygame.PixelArray(DISPLAYSURF)

main()
