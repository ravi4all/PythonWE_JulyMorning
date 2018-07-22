import pygame

pygame.init()

width = 1000
height = 600

# 0-255
black = 0,0,0
# white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width, height))

bg_img = pygame.image.load("assets/game_bg.jpg")
ball = pygame.image.load("assets/ball_2.png")

bgMusic = pygame.mixer.Sound("assets/theme.ogg")
bgMusic.play()

hitSound = pygame.mixer.Sound("assets/hit.wav")

x = 50
y = 50

move_x = 10
move_y = 10

clock = pygame.time.Clock()
FPS = 100

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit() # quit pygame
            quit() # quit python

    # screen.fill(red)
    screen.blit(bg_img, (0,0))
    # pygame.draw.circle(screen, black, [x,y], 50)
    screen.blit(ball, (x,y))
    x += move_x
    y += move_y

    if x >= width - (ball.get_width()/2):
        move_x = -10
        hitSound.play()
    elif x < 0:
        move_x = 10
        hitSound.play()
    if y >= height - (ball.get_height()/2):
        move_y = -10
        hitSound.play()
    elif y < 0:
        move_y = 10
        hitSound.play()

    pygame.display.update()
    clock.tick(FPS)