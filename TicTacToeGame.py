# TicTacToe 
# By Zach Kaufman exzachtlylast@gmail.com

import random, pygame, sys
from pygame.locals import *

FPS = 15
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
LIGHTGRAY = (192, 192, 192)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT # global variables for screen size
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('TicTacToe')

    showStartScreen()
    while True: # main games loop
        setUpGameScreen()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# Sets up the game screen for the game
def setUpGameScreen():
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, BLACK, (400, 40), (400, 440), 4)
    pygame.draw.line(DISPLAYSURF, BLACK, (200, 40), (200, 440), 4)
    pygame.draw.line(DISPLAYSURF, BLACK, (75, 160), (525, 160), 4)
    pygame.draw.line(DISPLAYSURF, BLACK, (75, 320), (525, 320), 4)

    # pixObj = pygame.PixelArray(DISPLAYSURF)


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
          terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen():
    titleFont = pygame.font.Font("freesansbold.ttf", 100)
    titleSurf1 = titleFont.render("TicTacToe!", True, DARKGRAY, RED)
    titleSurf2 = titleFont.render("TicTacToe!", True, LIGHTGRAY)

    degrees1 = 0
    degrees2 = 0

    while True:
        DISPLAYSURF.fill(WHITE)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7
                
def terminate():
    pygame.quit()
    sys.exit()
                                  
main()
