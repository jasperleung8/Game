import pygame
import os
from pygame.locals import QUIT

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT = 900,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space_game!")

WHITE = (255,255,255)
Black = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10,HEIGHT)

HITSOUND = pygame.mixer.Sound("Grenade+1.mp3")
FIRESOUND = pygame.mixer.Sound("Gun+Silencer.mp3")

HEALTHFONT = pygame.font.SysFont("comicsans",40)
WINNERFONT = pygame.font.SysFont("comicsans",100)

VEL = 5
FPS = 60
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("rocket1.png")
YELLOW_SPACESHIP_IMAGE = pygame.transfrom.scale(
    YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_WIDTH)))

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("rocket2.png")
RED_SPACESHIP_IMAGE = pygame.transfrom.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_WIDTH)))

BG =pygame.transform.scale(pygame.image.load(
    os.path.join('bg,jpeg')),(WIDTH,HEIGHT))

def draw_window(red,wellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(BG,(0,0))
    pygame.draw.rect(screen,Black,BORDER)

    red_health_text = HEALTHFONT.render(
        "Health:" + str(red_health),1,WHITE)
    yellow_health_text = HEALTHFONT.render(
        "health:" + str(yellow_health),1,WHITE)
    screen.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    screen.blit(yellow_health_text,(10,10))

    screen.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    screen.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(screen,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,YELLOW,bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL

    def handle_bullets(yellow_bullets,red_bullets,yellow,red):
        for bullet in yellow_bullets:
            bullet.x += BULLET_VEL
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                yellow_bullets.remove(bullet)
        
        for bullet in red_bullets:
            bullet.x += BULLET_VEL
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.remove(bullet)
            elif bullet.x > 0:
                red_bullets.remove(bullet)
            

def draw_winer(text):
    draw_text = WINNERFONT.render(text,1,WHITE)
    screen.blit(draw_text,(WIDTH/2 - draw_text.get_width()/
                           2,HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
