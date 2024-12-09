import pygame
from naves import *
from ventana import *

balas_1 = []
balas_2 = []
balas_velocidad= 7
maximo_balas = 3
#temporizador agregado después de tener problemas con mi el switch de mi teclado
#es switch red
tiempo_entre_disparos = 500  # 0.5 segundos
ultimo_disparo_jugador1 = 0
ultimo_disparo_jugador2 = 0

#evento de usuario para disparos
jugador1_hit= pygame.USEREVENT +1
jugador2_hit = pygame.USEREVENT + 2






#manejo de balas
def manejo_de_balas(balas_1, balas_2, jugador1, jugador2):
    for bala in balas_1:
        bala.x += balas_velocidad
        if jugador2.colliderect(bala):
            pygame.event.post(pygame.event.Event(jugador2_hit))
            balas_1.remove(bala)
        elif bala.x > WIDTH:
            balas_1.remove(bala)

    for bala in balas_2:
        bala.x -= balas_velocidad
        if jugador1.colliderect(bala):
            pygame.event.post(pygame.event.Event(jugador1_hit))
            balas_2.remove(bala)
        elif bala.x < 0:
            balas_2.remove(bala)

            
    