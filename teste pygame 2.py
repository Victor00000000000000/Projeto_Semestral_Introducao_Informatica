import pygame
from pygame.locals import *
from sys import exit

from auxiliar import Player_1

pygame.init()
#pygame.mixer.init()


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
#Sprite "knight"
knight = Player_1(drawGroup)
#knight = pygame.sprite.Sprite(drawGroup)
##knight.image = pygame.image.load(r"C:\Users\home\Desktop\Victor\UFSC\Pygame teste\Data\Imagens\knight.png")
##knight.rect = pygame.Rect(0, 0, 100, 100)
##knight.image = pygame.transform.scale(knight.image, (100,100))

    
#Sound's settings:
#Background Sound:
pygame.mixer.music.load(r"C:\Users\home\Desktop\Victor\UFSC\Pygame teste\Data\Áudios\Cyberpunk Moonlight Sonata.mp3")
pygame.mixer.music.play(-1)

#Shoot effect:
shoot_sound = pygame.mixer.Sound(r"C:\Users\home\Desktop\Victor\UFSC\Pygame teste\Data\Áudios\Spells\Shoot_sound\shot converter.mp3")
shoot_sound.set_volume(1.0)
while True:
    tela.fill((0, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT: #QUIT ao clicar X
            pygame.quit()
            exit()

        elif event.type == KEYDOWN:
            if event.key == pygame.K_w:
                knight.rect.y -= 1
                
            if event.key == pygame.K_a:
                knight.rect.x -= 1
                
            if event.key == pygame.K_d:
                knight.rect.x += 1

            if event.key == pygame.K_s:
                knight.rect.y += 1
                
            if event.key == K_SPACE:
                shoot_sound.play()
                
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        knight.rect.y -= 1
        
    if keys[pygame.K_a]:
        knight.rect.x -= 1

    if keys[pygame.K_d]:
        knight.rect.x += 1
        
    if keys[pygame.K_s]:
        knight.rect.y += 1
                
    drawGroup.draw(tela)
    #pygame.draw.rect(tela, color_ret, ret)




    
    drawGroup.draw(tela) #Desenha todos as imagens relacionadas a um objeto instânciado de .Sprite

    
    pygame.display.update()
