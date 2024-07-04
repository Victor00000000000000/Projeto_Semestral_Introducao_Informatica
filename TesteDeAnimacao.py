import pygame
from pygame.locals import *
from pygame.math import Vector2
from sys import exit

pygame.init()

tela = pygame.display.set_mode((1000, 500))

drawGroup = pygame.sprite.Group()

sprite_vector = Vector2(0, 0)
sprite_teste_1 = pygame.sprite.Sprite(drawGroup)
sprite_teste_1.image = pygame.image.load(r"Data\Imagens\knight.png")
sprite_teste_1.rect = pygame.Rect(sprite_vector, (10, 10))
sprite_teste_1.image = pygame.transform.scale(sprite_teste_1.image, (75, 75))

i = 0
sprite_vector2 = Vector2(100, 100)
sprite_teste_2 = pygame.sprite.Sprite(drawGroup)
sprite_teste_2.image = pygame.image.load(r"Data\Imagens\knight.png")
sprite_teste_2.rect = pygame.Rect(sprite_vector2, (10, 10))
sprite_teste_2.image = pygame.transform.scale(sprite_teste_2.image, (75, 75))
sprite_teste_2.image = pygame.transform.rotate(sprite_teste_1.image, i)

knight_left = True
knight_right = False
while True:
    tela.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                if not knight_right:
                    sprite_teste_1.image = pygame.transform.flip(sprite_teste_1.image, True, False)
                    knight_right = True
                    knight_left = False
                    
            if event.key == K_a:
                if not knight_left:
                    sprite_teste_1.image = pygame.transform.flip(sprite_teste_1.image, True, False)
                    knight_left = True
                    knight_right = False

    sprite_teste_2.image = pygame.transform.rotate(sprite_teste_1.image, i)
    i+=1

    key = pygame.key.get_pressed()
    if key[K_a]:
        sprite_teste_1.rect.x -= 1

    if key[K_d]:
        sprite_teste_1.rect.x += 1
        
    drawGroup.draw(tela, (0, 0))
    pygame.display.update()
