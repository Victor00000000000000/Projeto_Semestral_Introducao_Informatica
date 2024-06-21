import pygame
from pygame.locals import *
from sys import *
from pygame.math import *

pygame.init()

screen_dimentions = Vector2(700, 700)
screen_center = screen_dimentions // 2


tela = pygame.display.set_mode(screen_dimentions)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.line(tela, "red", (0, screen_center.y), (screen_dimentions.x, screen_center.y))
    pygame.draw.line(tela, "red", (screen_center.x, 0), (screen_center.x, screen_dimentions.y))
    retan = pygame.Rect(0, 0, 100, 100)
    pygame.draw.rect(tela, "blue", retan)
    pygame.draw.rect(tela, "red", retan)
    retan.center = (100,100)
    pygame.display.update()
    
