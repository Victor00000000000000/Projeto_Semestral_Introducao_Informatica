import math as m
import pygame
from pygame.locals import *
import random as r
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()

class Knight(pygame.sprite.Sprite):
    "Player's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vk = Vector2(300, 300)
        
        self.image = pygame.image.load(r"Data\Imagens\knight.png")
        self.rect = pygame.Rect(self.vk, (20, 40))
        self.image = pygame.transform.scale(self.image, (75,75))

        self.rect.center = (self.rect.x/2, self.rect.y/2)

        self.vk = Vector2(self.rect.x, self.rect.y)

        self.health = 1000

        self.vk = Vector2()
        
    def update(self, *arg):
        #Movimentação WASD do Knight
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.rect.y -= 3.5
        
        if keys[pygame.K_a]:
            self.rect.x -= 3.5
                    
        if keys[pygame.K_d]:
            self.rect.x += 3.5

        
        if keys[pygame.K_s]:
            self.rect.y += 3.5

        # Mudar para a tecla do mouse
        #shoot_sound = pygame.mixer.music.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Áudios\Spells\Shoot_sound\shot converter.mp3")
##        for event in pygame.event.get():
##            if event.type == MOUSEBUTTONDOWN:
##                shoot_sound.play()

##            if event.type == KEYDOWN:
##                if event.key == K_a:
##                    self.image = pygame.transform.scale(pygame.transform.flip(self.image, True, False), (75,75))
##
##                if event.key == K_d:
##                    self.image = pygame.transform.scale(pygame.transform.flip(self.image, True, False), (75,75))
                    
        #Colision of a Knight on walls
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > 480:
            self.rect.bottom = 480

        if self.rect.right > 650:
            self.rect.right = 650

        if self.rect.left < 0:
            self.rect.left = 0
