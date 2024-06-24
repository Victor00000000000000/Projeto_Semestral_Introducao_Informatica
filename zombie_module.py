import math as m
import pygame
from pygame.locals import *
import random as r
from pygame.math import Vector2
from knight_module import Knight
pygame.init()

class Zombie(pygame.sprite.Sprite):
    "Zombies' programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vz = Vector2()
        
        self.image = pygame.image.load(r"Data\Imagens\zombiePixel.png")
        self.rect = pygame.Rect(self.vz, (40, 40))
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect.x = r.randint(100, 400)
        self.rect.y = r.randint(40, 300)

        
        
        self.vz = Vector2(self.rect.x, self.rect.y)

        
        self.__knight = Knight()
        self.distance_zk = self.vz.distance_to(self.__knight.vk)
    
        self.health = 10

        #Criar o código para evitar que o Zombie seja gerado em cima do Knight

    def update(self, *args):#Zombie's movimetion 
        self.vz.move_towards_ip(self._knight.vk, self.distance_zk)
        
        
