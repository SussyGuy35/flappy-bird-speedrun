import pygame, sys, random

def game_reset():
    global is_started,bird,pipe_group,trigger_group,spw_time,spw_timer,reset_time,reset_timer,game_speed
    
    is_started = False

    bird = Bird(32,32,(screen_width/4,screen_height/2),(255,255,255),0.2,5)

    pipe_group = pygame.sprite.Group()
    trigger_group = pygame.sprite.Group()

    spw_time = 1.5 * game_speed
    spw_timer = spw_time

    reset_time = 3000
    reset_timer = pygame.USEREVENT+0

class Bird(pygame.sprite.Sprite):
    def die(self):
        if self.is_alive:
            pygame.time.set_timer(reset_timer,reset_time)
            self.is_alive = False
    def __init__(self,width,height,pos,color,grv,jump_force):
        super().__init__()
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(0,0,self.width,self.height)
        self.color = color
        self.rect.center = pos
        self.vsp = 0
        self.grv = grv
        self.jump_force = jump_force
        self.is_alive = True
        self.score = 0
    def update(self):
        if is_started: self.vsp += self.grv
        self.rect.y += self.vsp

        if self.rect.bottom < -self.height*2: self.rect.bottom = -self.height*2
        if self.rect.bottom > ground_y: self.die()

        if pygame.sprite.spritecollide(self,trigger_group,True): 
            self.score += 1

        if pygame.sprite.spritecollide(self,pipe_group,False):
            self.die()

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
        if is_started and bird.is_alive: self.rect.x -= self.move_speed

        if self.rect.right < 0: self.kill()

        self.draw()
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)

class PipeDown(pygame.sprite.Sprite):
    def __init__(self,color,x_pos,y_pos,move_speed,gap_height):
        super().__init__()
        self.rect = pygame.rect.Rect(0,0,64,1000)
        self.color = color
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.move_speed = move_speed
        self.gap_height = gap_height
        pipe_group.add(PipeUp((64,64,128),screen_width+20,self.rect.y - self.gap_height,4))
        trigger_group.add(Trigger(10,self.gap_height,self.rect.x+54,self.rect.y - self.gap_height,self.move_speed ))
    def update(self):    
        if is_started and bird.is_alive: self.rect.x -= self.move_speed

        if self.rect.right < 0: self.kill()

        self.draw()
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)

class Trigger(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,move_speed):
        super().__init__()
        self.rect = pygame.rect.Rect(pos_x,pos_y,width,height)
        self.move_speed = move_speed
    def update(self):
        if bird.is_alive: self.rect.x -= self.move_speed    


# Config
screen_width = 500
screen_height = 700
game_speed = 60
title = "Flappy bird"

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption(title)
font = pygame.font.Font("font.ttf",25)
# Sth
is_started = False

ground_y = screen_height-50

bird = Bird(32,32,(screen_width/4,screen_height/2),(255,255,255),0.2,5)

pipe_group = pygame.sprite.Group()
trigger_group = pygame.sprite.Group()

# spw_time = 1500
# spw_timer = pygame.USEREVENT+0
spw_time = 1.5 * game_speed
spw_timer = spw_time

reset_time = 2000
reset_timer = pygame.USEREVENT+0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if is_started == False: 
                is_started = True
                #pygame.time.set_timer(spw_timer,spw_time)
            
            if bird.is_alive: bird.vsp = -bird.jump_force
        # if event.type == spw_timer:
        #     pipe_group.add(PipeDown((64,64,128),screen_width+20,random.randint(150,screen_height-150),4,120))
        if event.type == reset_timer:
            game_reset()
            pygame.time.set_timer(reset_timer,0)

    if is_started: spw_timer -= 1
    if spw_timer == 0:
        pipe_group.add(PipeDown((64,64,128),screen_width+20,random.randint(150,screen_height-150),4,120))
        spw_timer = spw_time

    screen.fill((64,128,64))

    pygame.draw.rect(screen,(60,60,120),pygame.rect.Rect(0,ground_y,screen_width,screen_height-ground_y))

    pipe_group.update()
    bird.update()
    trigger_group.update()

    score_surf = font.render(str(bird.score),True,(255,255,255))
    score_rect = score_surf.get_rect()
    score_rect.center = (screen_width/2,screen_height/5)
    screen.blit(score_surf,score_rect)

    pygame.display.flip()
    clock.tick(game_speed)        