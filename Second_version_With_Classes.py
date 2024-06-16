import math as m
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
pygame.mixer.init()


#Surface's settings
tela_dimensions = (640, 480)
tela = pygame.display.set_mode(tela_dimensions)

#Color's settings
color_background = pygame.Color(0, 255, 255)
color_ret = pygame.Color(255, 0, 0)

#Rect's settings
ret = pygame.Rect(50, 50, 100, 100)

#Group's settings
drawGroup = pygame.sprite.Group()

#Sprite's settings
class Aim(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\aim.png")
        self.rect = pygame.Rect(11, 11, 0, 0)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self, *args):
        self.rect.x = pygame.mouse.get_pos[0]
        self.rect.y = pygame.mouse.get_pos[1]


class Zombie(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\spongeBob.png")
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.image = pygame.transform.scale(self.image, (100,100))

        self.timer = 0
    def update(self, *arg):
        self.timer += 0.1
        self.rect.x = 10*m.sin(self.timer)

    
class Knight(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\knight.png")
        self.rect = pygame.Rect(0, 0, 100, 100)
        self.image = pygame.transform.scale(self.image, (100,100))
        
    def update(self, *arg):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.rect.y -= 1
        
        if keys[pygame.K_a]:
            self.rect.x -= 1

        if keys[pygame.K_d]:
            self.rect.x += 1
        
        if keys[pygame.K_s]:
            self.rect.y += 1
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    shoot_sound.play()
                
                
#Sound's settings:
#Background Sound:
pygame.mixer.music.load(r"C:\Users\home\Desktop\Victor\UFSC\Pygame teste\Data\Áudios\Cyberpunk Moonlight Sonata.mp3")
pygame.mixer.music.play(-1)

#Shoot effect:
shoot_sound = pygame.mixer.Sound(r"C:\Users\home\Desktop\Victor\UFSC\Pygame teste\Data\Áudios\Spells\Shoot_sound\shot converter.mp3")
shoot_sound.set_volume(1.0)


#Clock's settings:
clock = pygame.time.Clock()

knight = Knight(drawGroup)
sponge_bob = Zombie(drawGroup)
#aim = Aim(drawGroup)
while True:
    tela.fill((0, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT: #QUIT ao clicar X
            pygame.quit()
            exit()
    #clock.tick(100)
    #print(list(pygame.event.get()))
    drawGroup.update()
    drawGroup.draw(tela)
    pygame.display.update()



