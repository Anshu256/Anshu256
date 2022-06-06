import pygame
from pygame.locals import *
from random import randint

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

WIDTH = 400
HEIGHT = 300
DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PONG")

WHITE = (255,255,255)
BLUE = (0,0,128)
RED = (255,0,0)
BLACK = (0,0,0)

PADDLELEN = 50
PADDLESPEED = 5

ball_speed = [1,2]
players_pos = ([20, 120],[360,120])
curr_player = 0
ball_pos = [200,150]

while True:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF, BLUE, players_pos[0], (players_pos[0][0], players_pos[0][1]+PADDLELEN), 5)
    pygame.draw.line(DISPLAYSURF,RED,players_pos[1],(players_pos[1][0], players_pos[1][1]+PADDLELEN), 5)
    pygame.draw.circle(DISPLAYSURF,BLACK,ball_pos,10,10)

    ball_pos = [ball_pos[0] + ball_speed[0], ball_pos[1] + ball_speed[1]]

    # checks if touching top or bottom horizontal
    ball_speed[1] *= -1 if ball_pos[1] >= HEIGHT or ball_pos[1] <= 0 else 1
    # checks if touching paddle 1
    if ball_pos[0] <= players_pos[0][0] and players_pos[0][1] < ball_pos[1] and ball_pos[1] < players_pos[0][1]+PADDLELEN:
        ball_speed[0] *= -1
        curr_player = 1
    # checks if touching paddle 2
    elif ball_pos[0] >= players_pos[1][0] and players_pos[1][1] < ball_pos[1] and ball_pos[1] < players_pos[1][1]+PADDLELEN:
        ball_speed[0] *= -1
        curr_player = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                players_pos[curr_player][1] -= PADDLESPEED

            elif event.key == K_DOWN:
                players_pos[curr_player][1] += PADDLESPEED

    pygame.display.update()
    fpsClock.tick(FPS)
