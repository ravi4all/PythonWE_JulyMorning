import pygame

pygame.init()

width = 1000
height = 500

# 0-255
# black = 0,0,0
# white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width, height))

screen.fill(red)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

    pygame.display.update()