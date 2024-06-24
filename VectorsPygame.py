import pygame
from pygame.locals import *
from sys import *
from pygame.math import Vector2
from random import randint
pygame.init()

screen_dimentions = Vector2(700, 450)
screen_center = screen_dimentions // 2
tela = pygame.display.set_mode(screen_dimentions)

drawGroup = pygame.sprite.Group()

class Person_2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super.__init__(*groups)
        
        self.vector2 = Vector2()
        self.image = pygame.image.load(r"Data\Imagens\spongeBob.png")
        self.rect = pygame.Rect(vector1, (10, 10))
        self.image = pygame.transform.scale(person_1.image, (100, 100))

        vector2 = Vector2(randint(400, 500), randint(10, 20))

class Person_1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super.__init__(*groups)
        
        self.vector1 = Vector2()
        self.image = pygame.image.load(r"Data\Imagens\spongeBob.png")
        self.rect = pygame.Rect(vector1, (10, 10))
        self.image = pygame.transform.scale(person_1.image, (100, 100))

        self.vector1 = Vector2(randint(200, 300), randint(100, 200))

        self.__person_2 = Person_2
        
        distance = self.vector1.distance_to(self.__person_2.vector2)

    def print(self, *args):
        print(distance)

person_1 = Person_1(drawGroup)
person_2 = Person_2(drawGroup)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    person_1.print()

    


    drawGroup.draw(tela)
    drawGroup.update(tela)
    
    pygame.display.update()
    
