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

    def update(self, *arg):
        #Coordenadas globais do knight e atualização dos valores
        global knight_x, knight_y, vector_k
        self.vk = Vector2(x=self.rect.x, y=self.rect.y)
        vector_k = self.vk
        knight_x = self.rect.x
        knight_y = self.rect.y
        
        
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
                

        # Animação Knight
##            if event.type == KEYDOWN:
##                if event.key == K_a:
##                    self.image = pygame.transform.scale(pygame.transform.flip(self.image, True, False), (75,75))
##
##                if event.key == K_d:
##                    self.image = pygame.transform.scale(pygame.transform.flip(self.image, True, False), (75,75))
                    
        #Colision of a Knight on walls
        if self.rect.top < 10:
            self.rect.top = 10

        if self.rect.bottom > 435:
            self.rect.bottom = 435

        if self.rect.right > 585:
            self.rect.right = 585

        if self.rect.left < 10:
            self.rect.left = 10
            
class Aim(pygame.sprite.Sprite):
    "Aim's programming"
    def __init__(self, *groups):##ERROR
        super().__init__(*groups)
        self.va = Vector2(300, 300)
        self.image = pygame.image.load(r"Data\Imagens\aim.png")
        self.rect = pygame.Rect(self.va, (0, 0))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.center = (150, 150)
    def update(self, *args):
        
        global aim_x, aim_y, aim_vector
        aim_x = self.rect.x
        aim_y = self.rect.y
        aim_vector = self.va

        mouse_visility = pygame.mouse.set_visible(False)
        mouse_coordenates = pygame.mouse.get_pos()
        self.rect.x = mouse_coordenates[0] - 25
        self.rect.y = mouse_coordenates[1] - 25

class Zombie(pygame.sprite.Sprite):
    "Zombies' programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vz = Vector2()
        
        self.image = pygame.image.load(r"Data\Imagens\zombiePixel.png")
        self.rect = pygame.Rect(self.vz, (40, 40))
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect.x = r.randint(10, 585)
        self.rect.y = r.randint(10, 435)

        
        
        self.vz = Vector2(self.rect.x, self.rect.y)

        
        self.distance_zk = self.vz.distance_to(vector_k)
    
        self.health = 10

        self.zombie_velocity = 1.5
        #Criar o código para evitar que o Zombie seja gerado em cima do Knight

    def update(self, *args):#Zombie's movimetion
        if self.distance_zk != 0:
            self.rect.x -= (self.zombie_velocity*(self.rect.x - knight_x))/self.distance_zk
            self.rect.y -= (self.zombie_velocity*(self.rect.y - knight_y))/self.distance_zk
        
        

class Bullet(pygame.sprite.Sprite):
    "FireBall's programming"
    
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.vb = Vector2()
        self.image = pygame.image.load(r"Data\Imagens\fireball.png")
        self.rect = pygame.Rect(self.vb, (80, 80))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.x = knight_x
        self.rect.y = knight_y
        self.shoot_sound = pygame.mixer.Sound(r"Data\Áudios\Spells\Shoot_sound\shot converter.mp3")
        self.angulo_aim_knight = m.atan2(aim_y-knight_y, aim_x-knight_x)
        self.velocity = 1
        
    def update(self, *args):
        global bullet_x, bullet_y, bullet_vector
        bullet_x = self.rect.x
        bullet_y = self.rect.y
        bullet_vector = self.vb
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                self.shoot_sound.play(1)
                self.rect.x += self.velocity
                self.rect.y += self.velocity*self.angulo_aim_knight
        
class Background(pygame.sprite.Sprite):
    "Scenario's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vbg = Vector2(0,0)
        self.image = pygame.image.load(r"Data\Imagens\Background.png")
        self.rect = pygame.Rect(self.vbg, (640, 480))
        self.image = pygame.transform.scale(self.image, (640, 480))        

