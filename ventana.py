import pygame
import os
from naves import *


#Ventana configs
WIDTH,HEIGHT = 1000, 500
ventana = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SpacialFight")
BORDE = pygame.Rect(WIDTH/2,0,10,HEIGHT)
borde_color=(0,0,0)


#carga de imagen FONDO

fondo_img =pygame.image.load(os.path.join('assets','fondo.png'))
# Redimensionar el fondo para que coincida con la ventana
fondo_img = pygame.transform.scale(fondo_img, (WIDTH, HEIGHT))

def dibujar_ventana(jugador1,jugador2):
    ventana.blit(fondo_img,(0,0))
    pygame.draw.rect(ventana,borde_color,BORDE)
    ventana.blit(nave_1,(jugador1.x,jugador1.y))
    ventana.blit(nave_2,(jugador2.x,jugador2.y))
    pygame.display.update()
