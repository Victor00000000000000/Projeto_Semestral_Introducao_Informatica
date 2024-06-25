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
        self.vk = Vector2(self.rect.x, self.rect.y)
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

        
        self.distance_zk = self.vz.distance_to(vector_k)
    
        self.health = 10


        #Criar o código para evitar que o Zombie seja gerado em cima do Knight

    def update(self, *args):#Zombie's movimetion
        #
##        global zombie_x, zombie_y
##        zombie_x = self.rect.x
##        zombie_y = self.rect.y 
##        vector_z = self.vz

        #self.vz = Vector2(self.rect.x, self.rect.y)         

        self.vz.move_towards_ip(vector_k, self.distance_zk)
        print(vector_k, knight_x, knight_y )

class Bullet(pygame.sprite.Sprite):
    "FireBall's programming"
    
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.vb = Vector2()
        self.image = pygame.image.load(r"Data\Imagens\fireball.png")
        self.rect = pygame.Rect(self.vb, (23, 17))
        self.image = pygame.transform.scale(self.image, (50, 50))

        #self.vb = Vector2(knight.rect.x, knight.rect.y)
        #self.distance = self.vb.distance_to(aim.va)
        
        
        #self.vb.move_towards_ip(aim.va, self.distance)
        
        
class Background(pygame.sprite.Sprite):
    "Scenario's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vbg = Vector2(0,0)
        self.image = pygame.image.load(r"Data\Imagens\Background.png")
        self.rect = pygame.Rect(self.vbg, (640, 480))
        self.image = pygame.transform.scale(self.image, (640, 480))        

