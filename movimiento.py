import pygame
from naves import *
from ventana import *



#movimiento de las naves
#defino velocidad
velocidad = 5

#movimiento de la nave 1


def movimiento_nave_1(keys_pressed,jugador1):
    if keys_pressed[pygame.K_a] and jugador1.x - velocidad >0: #izquierda
        jugador1.x -= velocidad
    if keys_pressed[pygame.K_d] and jugador1.x + velocidad +jugador1.width < BORDE.x: #derecha
        jugador1.x += velocidad
    if keys_pressed[pygame.K_w] and jugador1.y - velocidad >0: #arriba
        jugador1.y -= velocidad
    if keys_pressed[pygame.K_s]and jugador1.y + velocidad +jugador1.height < HEIGHT: #abajo
        jugador1.y += velocidad


#moviento de la nave 2

def movimiento_nave_2(keys_pressed,jugador2):
    if keys_pressed[pygame.K_LEFT]and jugador2.x - velocidad >BORDE.x+BORDE.width: #izquierda
        jugador2.x -= velocidad
    if keys_pressed[pygame.K_RIGHT]and jugador2.x + velocidad +jugador2.width < WIDTH: #derecha
        jugador2.x += velocidad
    if keys_pressed[pygame.K_UP]and jugador2.y - velocidad >0: #arriba
        jugador2.y -= velocidad
    if keys_pressed[pygame.K_DOWN]and jugador2.y + velocidad +jugador2.height < HEIGHT: #abajo
        jugador2.y += velocidad
