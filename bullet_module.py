import math as m
import pygame
from pygame.locals import *
import random as r
from pygame.math import Vector2
pygame.init()

class Bullet(pygame.sprite.Sprite):
    "FireBall's programming"
    
    def __init__(self, *groups):
        super().__init__(*groups)
        from aim_module import Aim
        from knight_module import Knight

        knight = Knight()
        aim = Aim()
        
        self.vb = Vector2()
        self.image = pygame.image.load(r"Data\Imagens\fireball.png")
        self.rect = pygame.Rect(self.vb, (23, 17))
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.vb = Vector2(knight.rect.x, knight.rect.y)
        self.distance = self.vb.distance_to(aim.va)
        
    def update(self, *args):
        from aim_module import Aim
        from knight_module import Knight

        knight = Knight()
        aim = Aim()

        
        
        self.vb.move_towards_ip(aim.va, self.distance)
