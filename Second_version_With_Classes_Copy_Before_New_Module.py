import pygame
from pygame.locals import *
from sys import exit
from ClassesModule import Knight, Zombie, Aim, Background
from random import random

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

#Rect's settings
ret = pygame.Rect(50, 50, 100, 100)

#Group's settings
drawGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()

#Sprite's settings
                
#Sound's settings:
#Background Sound:
pygame.mixer.music.load(r"C:\Users\home\Desktop\Victor\UFSC\Pygame teste\Data\Áudios\Cyberpunk Moonlight Sonata.mp3")
pygame.mixer.music.play(-1)

#Background's image:
##background = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Projeto_Semestral_Introducao_Informatica\Data\Imagens\Background.png")
##background.pygame.transform.scale(tela, (640, 480))

#Clock's settings:
clock = pygame.time.Clock()
background = Background(drawGroup)
knight = Knight(drawGroup)
sponge_bob = Zombie(drawGroup)
zombie_borner = 0.7
timer = 0
aim = Aim(drawGroup)
while True:
    clock.tick(60) # Define a quantidade de fps (60 fps
    mensage_health_knight = f"Health: {knight.health}" # Mensagem de vida do Knight
    texto_formatado_health = fonte.render(mensage_health_knight, True, color_text_health_knight) #Formatação da mensagem de vida do knight
    tela.blit(texto_formatado_health, (0, 0)) # Desenha o texto de vida do Knight
    
    texto_formatado_game_over = fonte.render("GAME OVER", True, color_text_end_game)
    
    for event in pygame.event.get():
        if event.type == QUIT: #QUIT ao clicar X
            pygame.quit()
            exit()

    timer+=1
    if timer > 30:# Gerador de Zombie's objects a cada 30 frames e com 30% de chance de spawn
        timer = 0
        if random() > zombie_borner:
            newZombie = Zombie(drawGroup, zombieGroup)


        collision = pygame.sprite.spritecollide(knight, zombieGroup, False)# COLISÃO DOS ZOMBIES COM O KNIGHT
        if collision:
            knight.health -= 5
            print(knight.health)


        if knight.health <= 0: #TELA DE GAME OVER
            tela.blit(texto_formatado_game_over, (320, 240))
            print("A vida é <= 0")
    
    
    drawGroup.update()
    drawGroup.draw(tela)
    pygame.display.update()



