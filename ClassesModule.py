import math as m
import pygame
from pygame.locals import *
import random as r
pygame.init()

class Aim(pygame.sprite.Sprite):
    "Aim's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"Data\Imagens\aim.png")
        self.rect = pygame.Rect(300, 300, 1, 1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.center = (150, 150)

    def update(self, *args):
        mouse_coordenates = pygame.mouse.get_pos()
        self.rect.x = mouse_coordenates[0] - 25
        self.rect.y = mouse_coordenates[1] - 25
                
                
class Zombie(pygame.sprite.Sprite):
    "Zombies' programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"Data\Imagens\zombiePixel.png")
        self.rect = pygame.Rect(100, 100, 25, 40)
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect.x = r.randint(100, 400)
        self.rect.y = r.randint(40, 300)

        self.health = 10

        if self.health <= 0:
            self.kill()

        
class Knight(pygame.sprite.Sprite):
    "Player's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"Data\Imagens\knight.png")
        self.rect = pygame.Rect(300, 300, 20, 40)
        self.image = pygame.transform.scale(self.image, (75,75))
        self.rect.center = (self.rect.x/2, self.rect.y/2)
        self.health = 100
        
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

class Bullet(pygame.sprite.Sprite):
    "FireBall's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"Data\Imagens\fireball.png")
        self.rect = pygame.Rect(200, 200, 23, 17)
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        #OBS: o comando MOUSEDOWN para disparar deve ser programado no arquivo main, mas as coordenadas da Bullet serão programadas dentro da classe
    def update(self, *arg):
        ang = m.atan2(self.rect.y-knight.rect.y, self.rect.x-knight.rect.x)
        
class Background(pygame.sprite.Sprite):
    "Scenario's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"Data\Imagens\Background.png")
        self.rect = pygame.Rect(0, 0, 640, 480)
        self.image = pygame.transform.scale(self.image, (640, 480))
