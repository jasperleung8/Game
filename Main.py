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



while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
