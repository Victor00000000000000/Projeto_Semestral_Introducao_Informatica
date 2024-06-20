import math as m
import pygame
from pygame.locals import *
import random as r
pygame.init()

###Shoot's settings
##shoot_sound = pygame.mixer.Sound(r"C:\Users\home\Desktop\Victor\UFSC\Pygame teste\Data\Áudios\Spells\Shoot_sound\shot converter.mp3")
##shoot_sound.set_volume(1.0)

class Aim(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\aim.png")
        self.rect = pygame.Rect(300, 300, 1, 1)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self, *args):
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
##              print("Mouse Moving")
                mouse_coordenates = pygame.mouse.get_pos()
##                self.rect.x = mouse_coordenates[0]
##                self.rect.y = mouse_coordenates[1]
                if event.rel[0] > 0:
                    self.rect.x = mouse_coordenates[0]
                
class Zombie(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\zombiePixel.png")
        self.rect = pygame.Rect(100, 100, 25, 40)
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect.x = r.randint(100, 400)
        self.rect.y = r.randint(40, 300)

        self.health = 10
        
##        self.timer = 0
##    def update(self, *arg):
##        self.timer += 0.1
##        self.rect.x = 10 + m.sin(self.timer) * 100

        if self.health <= 0:
            self.kill()

        
class Knight(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\knight.png")
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
     def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\fireball.png")
        self.rect = pygame.Rect(200, 200, 23, 17)
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        #OBS: o comando MOUSEDOWN para disparar deve ser programado no arquivo main, mas as coordenadas da Bullet serão programadas dentro da classe

class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\Background.png")
        self.rect = pygame.Rect(0, 0, 640, 480)
        self.image = pygame.transform.scale(self.image, (640, 480))
