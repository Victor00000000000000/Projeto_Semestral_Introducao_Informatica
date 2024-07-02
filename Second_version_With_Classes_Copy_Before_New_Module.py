import pygame
from pygame.locals import *
from sys import exit

from ClassesModule import Zombie, Knight, Zombie, Aim, Bullet, Background#, score_kill
from random import random
import math as m
from pygame.math import Vector2

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

pygame.init()

pygame.font.init()


#Surface's settings
tela_dimensions = (640, 480)
tela = pygame.display.set_mode(tela_dimensions)
pygame.display.set_caption("Knight Vs Zombies")

#Color's settings
color_background = pygame.Color(0, 255, 255)
color_ret = pygame.Color(255, 0, 0)
color_text_end_game = pygame.Color(255, 255, 255)
color_text_health_knight = pygame.Color(242, 41, 41)
color_menu = pygame.Color(100, 100, 100)
color_titulo = pygame.Color(70, 0, 0)
color_play = pygame.Color(70, 0, 0)
color_back_menu = pygame.Color(255, 255, 255)

#SysFont's settings:
fonte = pygame.font.SysFont("arial", 12, True, False)
fonte_end_game = pygame.font.SysFont("arial", 50, True, False)
fonte_health_knight = pygame.font.SysFont("arial", 30, True, False)
fonte_titulo = pygame.font.SysFont("arial", 70, True, False)
fonte_back_menu = pygame.font.SysFont("arial", 30, True, False)

#Group's settings
drawGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
                
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
aim = Aim(drawGroup)

zombie_borner = 0.7 #Porcentagem de chance de spawn da Zombie
timer = 0 # Variável auxiliar para o període de geração de Zombie's objects

#Variáveis booleanas auxiliares a troca de telas (menu, jogo e endgame)
game_over = True
music_game = True
music_menu = True

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



    #Aawfter empty drawGroup, bulletGroup, zombieGroup
    #print(list(drawGroup))       
    if len(drawGroup.sprites()) == 0: #PROBLEMAS, MUITO PROBLEMAS, A MIRA NÃO É REDESENHADA
            drawGroup.add(background)
            drawGroup.add(knight)
            drawGroup.add(aim)

    
 

    #MENU GAME
    if game_over and knight.health > 0:
        if music_menu:
            pygame.mixer.music.load(r"Data\Áudios\CrystalCave.mp3")
            pygame.mixer.music.play(-1)
            music_menu = False
        tela.fill(color_menu)
        texto_formatado_titulo = fonte_titulo.render("\nKnight\nVs\nZombies\n", True, color_titulo)
        tela.blit(texto_formatado_titulo, ((tela_dimensions[0]/2)-270, (tela_dimensions[1]/2)-200))
        texto_formatado_play = fonte_titulo.render("START", True, color_play)
        tela.blit(texto_formatado_play,((tela_dimensions[0]/2)-90, (tela_dimensions[1]/2)))



        #Programação PLAY
        # 230<= x <= 300
        # 240<= y <= 310
        mouse_coordenates = pygame.mouse.get_pos()
        if mouse_coordenates[0] >= 230 and mouse_coordenates[1] >= 240 and mouse_coordenates[0] <= 400 and mouse_coordenates[1]<=310:
            color_play = (140, 0, 0)
            print("Mouse dentro")
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    #print("Mouse clicado")
                    pygame.mixer.music.stop()
                    game_over = False
        else:
            color_play = (70, 0, 0)




    #START GAME
    if not game_over: #logic game execution
        #print(score_kill_imported)



        #MUSIC
        if music_game:
            pygame.mixer.music.load(r"Data\Áudios\Cyberpunk Moonlight Sonata.mp3")
            pygame.mixer.music.play(-1)
            music_game = False





        #Spawner    
        timer+=1
        if timer > 30:# Gerador de Zombie's objects a cada 30 frames e com 30% de chance de spawn
            timer = 0
            if random() > zombie_borner:
                pass
                #newZombie = Zombie(drawGroup, zombieGroup)
                #score_kill_imported = score_kill

                
            



        #Collisions:
        collision_knight_zombies = pygame.sprite.spritecollide(knight, zombieGroup, False)# COLISÃO DOS ZOMBIES COM O KNIGHT
        if collision_knight_zombies:
            knight.health -= 5

        collision_zombies_bullet = pygame.sprite.groupcollide(zombieGroup, bulletGroup, False, True)
        if collision_zombies_bullet:
            #for zombie in zombieGroup.sprites():
            newZombie.health -= 5# Só dimnui a vida do último gerado, consertar

            




        #Creating Bullet:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                bullet = Bullet(drawGroup, bulletGroup)

            



        #Animation:
 
        

            
        drawGroup.update()
        drawGroup.draw(tela)
        
        #End game Cases:
        if knight.health <= 0: #TELA DE GAME OVER
            tela.blit(texto_formatado_game_over, (200, 200))
            print("A vida é <= 0")
            game_over = True

            pygame.mixer.music.stop()#GAME OVER MUSIC
            pygame.mixer.music.load(r"Data\Áudios\Game-over_convertido.mp3")
            pygame.mixer.music.play()
            pygame.mouse.set_visible(True)
        




        #Status do knight:
        tela.blit(texto_formatado_health, (0, 0)) # Desenha o texto de vida do Knight








    #BACK TO MENU
    if knight.health <= 0:
        texto_back_menu_formatado = fonte_back_menu.render("Back to Menu", True, color_back_menu)
        tela.blit(texto_back_menu_formatado, (250, 300))
        # 250 <= x <= 350
        # 300 <= y <= 330
 
        #Programação do botão back
        mouse_coordenates = pygame.mouse.get_pos()
        if mouse_coordenates[0] >= 250 and mouse_coordenates[0] <= 410 and mouse_coordenates[1] >= 300 and mouse_coordenates[1] <= 330:
            color_back_menu = (200, 200, 200)
            print("Back Menu")
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    print("Mouse clicado")
                    knight.health = 1000
                    pygame.mixer.music.stop()

                    music_game = True
                    music_menu = True
                    
                    drawGroup.empty()
                    bulletGroup.empty()
                    zombieGroup.empty()
                    
        else:
            color_back_menu = (255, 255, 255)






            
    pygame.display.update()



