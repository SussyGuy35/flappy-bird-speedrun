import pygame, sys



# Config
screen_width = 500
screen_height = 700
game_speed = 60
title = "Flappy bird"

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption(title)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.flip()
    clock.tick(game_speed)        