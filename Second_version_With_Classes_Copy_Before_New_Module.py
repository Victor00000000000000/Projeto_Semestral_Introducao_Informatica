import pygame
from pygame.locals import *
from sys import exit

from ClassesModule import Zombie, Knight, Zombie, Aim, Bullet, Background
from random import random
import math as m
from pygame.math import Vector2

pygame.init()
pygame.mixer.init()
pygame.font.init()


#Surface's settings
tela_dimensions = (640, 480)
tela = pygame.display.set_mode(tela_dimensions)

#Color's settings
color_background = pygame.Color(0, 255, 255)
color_ret = pygame.Color(255, 0, 0)
color_text_end_game = pygame.Color(255, 255, 255)
color_text_health_knight = pygame.Color(242, 41, 41)

#SysFont's settings:
fonte = pygame.font.SysFont("arial", 12, True, False)
fonte_end_game = pygame.font.SysFont("arial", 50, True, False)
fonte_health_knight = pygame.font.SysFont("arial", 30, True, False)

#Rect's settings
ret = pygame.Rect(50, 50, 100, 100)

#Group's settings
drawGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

#Sprite's settings
                
#Sound's settings:
#Background Sound:
pygame.mixer.music.load(r"Data/Áudios/Cyberpunk Moonlight Sonata.mp3")
pygame.mixer.music.play(-1)

#Background's image:
#Clock's settings:
clock = pygame.time.Clock()

#Declarando obejtos de classes:
background = Background(drawGroup)
knight = Knight(drawGroup)
zombie_borner = 0.7 #Porcentagem de chance de spawn da Zombie
timer = 0
aim = Aim(drawGroup)
#bob = Bob(drawGroup)
game_over = False
number_zombie = -1
while True:
    clock.tick(60) # Define a quantidade de fps (60 fps
    mensage_health_knight = f"Health: {knight.health}" # Mensagem de vida do Knight
    texto_formatado_health = fonte_health_knight.render(mensage_health_knight, True, color_text_health_knight) #Formatação da mensagem de vida do knight
    texto_formatado_game_over = fonte_end_game.render("GAME OVER", True, color_text_end_game)
    
    for event in pygame.event.get():
        if event.type == QUIT: #QUIT ao clicar X
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN and not game_over:
            newBullet = Bullet(drawGroup, bulletGroup)

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_over = True

    if not game_over: #logic game execution
        #Spawner    
        timer+=1
        if timer > 30:# Gerador de Zombie's objects a cada 30 frames e com 30% de chance de spawn
            timer = 0
            if random() > zombie_borner:
                newZombie = Zombie(drawGroup, zombieGroup)
                number_zombie += 1
                
        #BULLET:
        
            
        #Collisions:
        collision_knight_zombies = pygame.sprite.spritecollide(knight, zombieGroup, False)# COLISÃO DOS ZOMBIES COM O KNIGHT
        if collision_knight_zombies:
            knight.health -= 5

        collision_zombies_bullet = pygame.sprite.groupcollide(zombieGroup, bulletGroup, False, False)
        if collision_zombies_bullet:
            newZombie.health -= 5

        #Animation:
##        keys = pygame.key.get_pressed()
##        if keys[pygame.K_a]:
##            knight.image.transform.flip(knight.image, False, True)
##
##        if keys[pygame.K_d]:
##            knight.image.transform.flip(knight.image, False, True)
            
        #End game Cases:
        #aim.update()
        drawGroup.update()
        drawGroup.draw(tela)

        if knight.health <= 0: #TELA DE GAME OVER
            tela.blit(texto_formatado_game_over, (200, 200))
            print("A vida é <= 0")
            game_over = True

        #Status do knight:
        tela.blit(texto_formatado_health, (0, 0)) # Desenha o texto de vida do Knight
    

        
    pygame.display.update()



