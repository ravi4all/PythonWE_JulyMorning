import pygame
import random

pygame.init()

width = 1000
height = 500

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width, height))

def game():

    myShip = pygame.image.load("images/ship_1.png")
    enemyShip = pygame.image.load("images/enemy_2.png")

    myShipWidth = myShip.get_width()
    myShipHeight = myShip.get_height()
    myShipX = width/2 - myShipWidth/2
    myShipY = height - myShipHeight

    enemyWidth = enemyShip.get_width()
    enemyHeight = enemyShip.get_height()

    columns = int(width/enemyShip.get_width())
    # print(int(columns))
    enemyList = []
    for i in range(columns*2):
        enemyList.append(enemyShip)

    moveX = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit pygame
                quit() # quit python

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 1
                elif event.key == pygame.K_LEFT:
                    moveX = -1

            elif event.type == pygame.KEYUP:
                moveX = 0

        screen.fill(white)

        for i in range(2):
            for j in range(int(len(enemyList)/2)):
                screen.blit(enemyList[i], (enemyWidth * j, enemyHeight * i))

        screen.blit(myShip, (myShipX, myShipY))

        myShipX += moveX

        if myShipX > width - myShipWidth:
            moveX = 0
        elif myShipX < 0:
            moveX = 0

        pygame.display.update()

game()