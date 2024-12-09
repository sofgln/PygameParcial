import pygame
import os
from naves import *
pygame.font.init()
pygame.mixer.init()



#Ventana configs
WIDTH,HEIGHT = 1000, 500
ventana = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SpacialFight")
BORDE = pygame.Rect(WIDTH//2,0,10,HEIGHT)
borde_color=(0,0,0)
color_rojo = (255,0,0)
color_blanco=(255,255,255)
color_amarillo=(248,243,43)
salud_font = pygame.font.SysFont('arial',40)
ganador_font= pygame.font.SysFont('arial',100)
sonido_bala_impacto=pygame.mixer.Sound('assets/collision.mp3')
sonido_bala_disparo=pygame.mixer.Sound('assets/disparo.mp3')
#musica de fondo
#def musica_de_fondo():
    #pygame.mixer.init()
    #pygame.mixer.Sound('assets/supershy.mp3')
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.5)

#carga de imagen FONDO

fondo_img =pygame.image.load(os.path.join('assets','fondo.png'))
# Redimensionar el fondo para que coincida con la ventana
fondo_img = pygame.transform.scale(fondo_img, (WIDTH, HEIGHT))

def dibujar_ganador(texto_ganador):
    texto_dibujado = ganador_font.render(texto_ganador,1,color_blanco)
    ventana.blit(texto_dibujado,(WIDTH/2 -texto_dibujado.get_width()/2,HEIGHT/2-texto_dibujado.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def dibujar_ventana(jugador1,jugador2,balas_1,balas_2,vida_jugador1,vida_jugador2):
    ventana.blit(fondo_img,(0,0))
    pygame.draw.rect(ventana,borde_color,BORDE)

    salud_2_texto = salud_font.render(
        "Salud: " + str(vida_jugador2), 1, color_blanco)
    salud_1_texto = salud_font.render(
        "Salud: " + str(vida_jugador1), 1, color_blanco)
    ventana.blit(salud_2_texto, (WIDTH - salud_2_texto.get_width() - 10, 10))
    ventana.blit(salud_1_texto, (10, 10))

    ventana.blit(nave_1,(jugador1.x,jugador1.y))
    ventana.blit(nave_2,(jugador2.x,jugador2.y))

    for bala in balas_1:
        pygame.draw.rect(ventana,color_amarillo,bala)
    
    for bala in balas_2:
        pygame.draw.rect(ventana,color_rojo,bala)

    pygame.display.update()
