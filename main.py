import pygame, sys, random

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

        self.draw()
    def draw(self):
        pygame.draw.ellipse(screen,self.color,self.rect)

class PipeUp(pygame.sprite.Sprite):
    def __init__(self,color,x_pos,y_pos,move_speed):
        super().__init__()
        self.rect = pygame.rect.Rect(0,0,64,1000)
        self.color = color
        self.rect.x = x_pos
        self.rect.bottom = y_pos
        self.move_speed = move_speed
    def update(self):    
        self.rect.x -= self.move_speed

        if self.rect.right < 0: self.kill()

        self.draw()
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)

class PipeDown(pygame.sprite.Sprite):
    def __init__(self,color,x_pos,y_pos,move_speed):
        super().__init__()
        self.rect = pygame.rect.Rect(0,0,64,1000)
        self.color = color
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.move_speed = move_speed
        pipe_group.add(PipeUp((64,64,128),screen_width+20,self.rect.y - 120,4))
    def update(self):    
        self.rect.x -= self.move_speed

        if self.rect.right < 0: self.kill()

        self.draw()
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)

# Config
screen_width = 500
screen_height = 700
game_speed = 60
title = "Flappy bird"

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption(title)

# Sth
bird = Bird(32,32,(screen_width/4,screen_height/2),(255,255,255),0.2,5)

pipe_group = pygame.sprite.Group()

spw_time = 3000
spw_timer = pygame.USEREVENT+0
pygame.time.set_timer(spw_timer,spw_time)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            bird.vsp = -bird.jump_force
        if event.type == spw_timer:
            pipe_group.add(PipeDown((64,64,128),screen_width+20,random.randint(100,screen_height-100),4))

    screen.fill((64,128,64))

    bird.update()
    pipe_group.update()

    pygame.display.flip()
    clock.tick(game_speed)        