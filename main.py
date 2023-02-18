import pygame, sys

class Bird(pygame.sprite.Sprite):
    def __init__(self,width,height,pos,color,grv,jump_force):
        super().__init__()
        self.rect = pygame.rect.Rect(0,0,width,height)
        self.color = color
        self.rect.center = pos
        self.vsp = 0
        self.grv = grv
        self.jump_force = jump_force
    def update(self):
        self.vsp += self.grv
        self.rect.y += self.vsp
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
bird = Bird(32,32,(screen_width/4,screen_height/2),(255,255,255),0.3,7)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            bird.vsp = -bird.jump_force


    screen.fill((64,128,64))

    bird.update()
    bird.draw()

    pygame.display.flip()
    clock.tick(game_speed)        