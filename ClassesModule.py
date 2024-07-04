import math as m
import pygame
from pygame.locals import *
import random as r
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()

##global bottom_zombie, top_zombie, right_zombie, left_zombie
##bottom_zombie = 0
##top_zombie = 0
##right_zombie = 0
##left_zombie = 0

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

        self.knight_right = False
        self.knight_left = True

    def update(self, *arg):
        #Coordenadas globais do knight e atualização dos valores
        global knight_x, knight_y, vector_k #Definindo algumas variáveis globais para que possam ser acessadas por outras classes
        self.vk = Vector2(x=self.rect.x, y=self.rect.y)
        vector_k = self.vk
        knight_x = self.rect.x
        knight_y = self.rect.y
        

        #Animação de movimento (Esquerda e Direita)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_a:
                    if not self.knight_left:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.knight_left = True
                        self.knight_right = False

                if event.key == K_d:
                    if not self.knight_right:
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.knight_left = False
                        self.knight_right = True
        
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

        #Colision of a Knight on walls
        if self.rect.top < 10:
            self.rect.top = 10
            print(self.rect.top, "top")

        if self.rect.bottom > 435:
            self.rect.bottom = 435
            print(self.rect.bottom, "bottom")

        if self.rect.right > 585:
            self.rect.right = 585
            print(self.rect.right, "right")

        if self.rect.left < 10:
            self.rect.left = 10
            print(self.rect.left, "left")


        #Colision with zombies
##        if self.rect.top >= top_zombie:
##            self.rect.y -= 10
##
##        if self.rect.bottom <= bottom_zombie:
##            self.rect.y += 10
##
##        if self.rect.right >= right_zombie:
##            self.rect.x -= 10
##
##        if self.rect.left <= left_zombie:
##            self.rect.x += 10
            
            
class Aim(pygame.sprite.Sprite):
    "Aim's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.va = Vector2(300, 300)
        self.image = pygame.image.load(r"Data\Imagens\aim.png")
        self.rect = pygame.Rect(self.va, (0, 0))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.center = (150, 150)
    def update(self, *args):
        
        global aim_x, aim_y, aim_vector #Definindo algumas variáveis globais para que possam ser acessadas por outras classes
        aim_x = self.rect.x
        aim_y = self.rect.y
        aim_vector = self.va

        mouse_visility = pygame.mouse.set_visible(False)
        mouse_coordenates = pygame.mouse.get_pos()

        self.rect.x = mouse_coordenates[0] - 25 #Posiciona o sprite da aim no cursor e atualiza a posição
        self.rect.y = mouse_coordenates[1] - 25
        

class Zombie(pygame.sprite.Sprite):
    "Zombies' programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vz = Vector2()
        
        self.image = pygame.image.load(r"Data\Imagens\zombiePixel.png")
        self.rect = pygame.Rect(self.vz, (40, 40))
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect.x = r.randint(10, 585)#Gera uma posição de spawn aleatória para o objeto newZombie
        self.rect.y = r.randint(10, 435)
        
        self.vz = Vector2(self.rect.x, self.rect.y) #Define um vetor posição para o newZombie

        
        self.distance_zk = self.vz.distance_to(vector_k)#Calcula a distância entre o vetor posição do newZombie e do knight
    
        self.health = 10

        self.zombie_velocity = 1.5
        #Criar o código para evitar que o Zombie seja gerado em cima do Knight

    def update(self, *args):#Zombie's movimetion
        global bottom_zombie, top_zombie, right_zombie, left_zombie #Definindo algumas variáveis globais para que possam ser acessadas por outras classes
        bottom_zombie = self.rect.bottom
        top_zombie = self.rect.top
        right_zombie = self.rect.right
        left_zombie = self.rect.left
        
        if self.distance_zk != 0:
            self.rect.x -= (self.zombie_velocity*(self.rect.x - knight_x))/self.distance_zk
            self.rect.y -= (self.zombie_velocity*(self.rect.y - knight_y))/self.distance_zk




class Bullet(pygame.sprite.Sprite):
    "FireBall's programming"
    
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.vb = Vector2()
        self.image = pygame.image.load(r"Data\Imagens\fireball.png")#.convert_alpha()
        self.rect = pygame.Rect(self.vb, (80, 80))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.shoot_sound = pygame.mixer.Sound(r"Data\Áudios\Spells\Shoot_sound\shot converter.mp3")

        #aim_y-knight_y, aim_x-knight_x
        
        self.rect.x = knight_x #Para gerar a posição inicial da Bullet na mesma coordenada do knight
        self.rect.y = knight_y


        self.dx = (aim_x-knight_x)#Verificando as diferenças das distâncias entre a aim e o knight em x e y
        self.dy = (aim_y-knight_y)

        self.distance_ka = vector_k.distance_to(aim_vector)

        self.angulo_aim_knight = m.atan2(aim_x-knight_x, aim_y-knight_y)

        self.velocity = 2

        #Defini o ângulo da imagem ao gerar o objeto
        self.image = pygame.transform.rotate(self.image, self.angulo_aim_knight)##############################################ERRO DESGRAÇADO
        
                
    def update(self, *args):
        #print(m.atan2((knight_y - aim_y), (knight_x - aim_x)))
        self.rect.x += self.velocity*(self.dx/self.distance_ka) 
        self.rect.y += self.velocity*(self.dy/self.distance_ka)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                self.shoot_sound.play(1)

        
         
class Background(pygame.sprite.Sprite):
    "Scenario's programming"
    def __init__(self, *groups):
        super().__init__(*groups)
        self.vbg = Vector2(0,0)
        self.image = pygame.image.load(r"Data\Imagens\Background.png")
        self.rect = pygame.Rect(self.vbg, (640, 480))
        self.image = pygame.transform.scale(self.image, (640, 480))    


