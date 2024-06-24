import math as m
import pygame
from pygame.locals import *
import random as r
from pygame.math import Vector2
pygame.init()

class Aim(pygame.sprite.Sprite):
    "Aim's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.va = Vector2(300, 300)
        self.image = pygame.image.load(r"Data\Imagens\aim.png")
        self.rect = pygame.Rect(self.va, (1, 1))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.center = (150, 150)

    def update(self, *args):
        mouse_visility = pygame.mouse.set_visible(False)
        mouse_coordenates = pygame.mouse.get_pos()
        self.rect.x = mouse_coordenates[0] - 25
        self.rect.y = mouse_coordenates[1] - 25
