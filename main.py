import pygame, sys

class Bird(pygame.sprite.Sprite):
    def __init__(self,width,height,pos,color):
        super().__init__()
        self.rect = pygame.rect.Rect(0,0,width,height)
        self.color = color
        self.rect.center = pos
    def update(self):
        pass
    def draw(self):
        pygame.draw.ellipse(screen,self.color,self.rect)


# Config
screen_width = 500
screen_height = 700
game_speed = 60
title = "Flappy bird"

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption(title)

# Sth
bird = Bird(32,32,(screen_width/4,screen_height/2),(255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((64,128,64))

    bird.draw()

    pygame.display.flip()
    clock.tick(game_speed)        