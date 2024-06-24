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

        

        self.health = 100

        self.vk = Vector2(self.rect.x, self.rect.y)
        
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
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    shoot_sound.play()

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
        from knight_module import Knight #Importanto a classe Knight para dentro da classe Zombie para poder trabalhar em conjunto com as variáveis de ambas
        knight = Knight()
        self.vz = Vector2()
        
        self.image = pygame.image.load(r"Data\Imagens\zombiePixel.png")
        self.rect = pygame.Rect(self.vz, (40, 40))
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect.x = r.randint(100, 400)
        self.rect.y = r.randint(40, 300)

        
        
        self.vz = Vector2(self.rect.x, self.rect.y)

        #self.distance_zk = self.vz.distance_to(knight.vk)
        
    
        self.health = 10

        #Criar o código para evitar que o Zombie seja gerado em cima do Knight
    def update(self, *args):#Zombie's movimetion 
        from knight_module import Knight #Importanto a classe Knight para dentro da classe Zombie para poder trabalhar em conjunto com as variáveis de ambas
        knight = Knight()

        self.vz.move_towards_ip(knight.vk, 5)
       
        
##            
##        zombie_speed = 1
##        d = Vector2(self.rect.x - knight.rect.x, self.rect.y - knight.rect.y)
##        #d = m.sqrt((self.rect.x-knight.rect.x)**2 + (self.rect.y-knight.rect.y)**2)
##        if d != 0:
##            self.rect.x += zombie_speed*d[0]
##            self.rect.y += zombie_speed*d[1]


class Bullet(pygame.sprite.Sprite):
    "FireBall's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vb = Vector2(200, 200)
        self.image = pygame.image.load(r"Data\Imagens\fireball.png")
        self.rect = pygame.Rect(self.vb, (23, 17))
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        
class Background(pygame.sprite.Sprite):
    "Scenario's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vbg = Vector2(0,0)
        self.image = pygame.image.load(r"Data\Imagens\Background.png")
        self.rect = pygame.Rect(self.vbg, (640, 480))
        self.image = pygame.transform.scale(self.image, (640, 480))

        

