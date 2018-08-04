import pygame
import random

pygame.init()

width = 1000
height = 500

# 0-255
black = 0,0,0
white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width, height))

img = pygame.image.load("frog.png")
imgX = random.randint(0,width - img.get_width())
imgY = random.randint(0,height - img.get_height())

x = 0
y = 0

moveX = 0
moveY = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0

    screen.fill(white)
    screen.blit(img, (imgX, imgY))
    rect1 = pygame.draw.rect(screen, red, [x,y,50,50])
    rect2 = pygame.Rect(imgX, imgY, img.get_width(), img.get_height())

    if rect1.colliderect(rect2):
        imgX = random.randint(0, width - img.get_width())
        imgY = random.randint(0, height - img.get_height())

    x += moveX
    y += moveY

    if x > width - 50:
        moveX = 0
    elif x < 0:
        moveX = 0
    if y > height - 50:
        moveY = 0
    elif y < 0:
        moveY = 0

    pygame.display.update()