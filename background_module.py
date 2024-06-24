import math as m
import pygame
from pygame.locals import *
import random as r
from pygame.math import Vector2
pygame.init()

class Background(pygame.sprite.Sprite):
    "Scenario's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vbg = Vector2(0,0)
        self.image = pygame.image.load(r"Data\Imagens\Background.png")
        self.rect = pygame.Rect(self.vbg, (640, 480))
        self.image = pygame.transform.scale(self.image, (640, 480))
