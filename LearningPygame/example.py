"""
Pygame

Basically you have to get a DisplayCanvas to show the game.
pygame.init() will give you a empty application and it will be in the variable pygame
so if u want to refer to the screen , you have to do it through pygame

Pygame object works on recording the events happening inside the screen.
so that it can be used to manipulate.

"""
import random

import pygame , duallog , logging , time
from pyautogui import size

height, width = (800, 800)  # size()

def log():
    duallog.setup("Logs")
    return logging.getLogger()
def pygameInit():
    pygame.init()
    gameDisplay = pygame.display.set_mode((height, width))  # set_mode takes tuple as an Arg
    pygame.display.set_caption("An Example Game.")
    return gameDisplay

gameDisplay = pygameInit()

clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73


carImg = pygame.image.load("racecar.png")

def car(x,y):
    gameDisplay.blit(carImg,(x,y)) #Blit is used to draw images to the gameDisplay.

def gameQuit():
    pygame.quit()
    quit()

def gameUpdate():
    pygame.display.update()
    clock.tick(60)

def gameBoundaryExitCheck(x,y):
    if x > width - car_width or x < 0:
        crash()
    if y > height - car_width or y < 0:
        crash()

def gameTextObjects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface , textSurface.get_rect()

def gameObjects(objectX,objectY,objectW,objectH,color):
    pygame.draw.rect(gameDisplay,color,[objectX,objectY,objectW,objectH])

def message_display(text):
    largeText = pygame.font.Font('FreeSansBold.ttf',50)
    TextSurf , TextRect = gameTextObjects(text,largeText)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)

def crash():
    message_display("You Crashed! Game Over!")
    gameLoop()

def gameLoop():
#
    x = (width * 0.5)
    y = (height * 0.5)
    x_change = 0
    y_change = 0
    car_speed = 0
    print(x,y)
    gameExit = False
    ##
    object_startX = random.randrange(0,width)
    object_startY = -100
    object_speed = 7
    object_width = 100
    object_height = 100
    ##
    while not gameExit:
            ####
        for event in pygame.event.get():
            log().debug(f"Event : {event}")
            if event.type == pygame.QUIT:
                gameQuit()

            ####
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            ####
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            ####
        x += x_change
        y += y_change
        ###
        gameDisplay.fill(white)
        gameObjects(object_startX,object_startY,object_width,object_height,black)
        object_startY += object_speed
        car(x,y)
        gameBoundaryExitCheck(x, y)
        ## This is used to reset the blocks coming in.
            ## How this works is , It checks the Object's Y Co-ordinate to see if it has
            ## Surpassed the window height.
            ## if it has surprassed , we reset the block to have 0 - object_height
            ## and Random place in the Screen -> object_startX
        if object_startY > height:
            object_startY = 0 - object_height
            object_startX = random.randrange(0,width)

        gameUpdate()
        ###

    ##
    gameQuit()
#

gameLoop()
gameQuit()




