import pygame
import os

#vida de cada jugador
vida_jugador1 = 100
vida_jugador2 = 100

#dimensiones naves
naves_ancho, naves_alto = 120,100

#carga de imagenes de las naves

nave_1 = pygame.image.load(os.path.join('assets','nave1.png'))
nave_2 = pygame.image.load(os.path.join('assets','nave2.png'))

#redimension naves
nave_1 = pygame.transform.scale(nave_1, (naves_ancho,naves_alto))
nave_2 = pygame.transform.scale(nave_2, (naves_ancho,naves_alto))

#rectangulos naves
jugador1=pygame.Rect(200,100,naves_ancho,naves_alto) 
jugador2=pygame.Rect(700,100,naves_ancho,naves_alto)