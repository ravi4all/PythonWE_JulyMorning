import pygame

pygame.init()

width = 1000
height = 500

# 0-255
black = 0,0,0
# white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width, height))

x = 50
y = 50

move_x = 3
move_y = 3

clock = pygame.time.Clock()
FPS = 100

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

    screen.fill(red)
    pygame.draw.circle(screen, black, [x,y], 50)

    x += move_x
    y += move_y

    if x >= width - 50:
        move_x = -3
    elif x < 50:
        move_x = 3
    if y >= height - 50:
        move_y = -3
    elif y < 50:
        move_y = 3

    pygame.display.update()
    clock.tick(FPS)