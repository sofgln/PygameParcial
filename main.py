import pygame
pygame.font.init()
from ventana import *
from naves import *
from movimiento import *
from disparos import *

#fps

FPS=60








#función principal
def main():
    global ultimo_disparo_jugador1, ultimo_disparo_jugador2, jugador1_hit,jugador2_hit,vida_jugador1,vida_jugador2,sonido_bala_disparo,sonido_bala_impacto
    clock= pygame.time.Clock()
    run= True
    while run:
        clock.tick(FPS)
        tiempo_actual = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
                
            
            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_LCTRL and len(balas_1)< maximo_balas:
                    if tiempo_actual - ultimo_disparo_jugador1 > tiempo_entre_disparos:
                        bala= pygame.Rect(jugador1.x + jugador1.width, jugador1.y + jugador1.height//2 - 2, 10, 5)
                        balas_1.append(bala)
                        sonido_bala_disparo.play()
                        ultimo_disparo_jugador1 = tiempo_actual
        
        
                if event.key ==pygame.K_RCTRL and len(balas_2)< maximo_balas:
                    if tiempo_actual - ultimo_disparo_jugador2 > tiempo_entre_disparos:
                        bala= pygame.Rect(jugador2.x , jugador2.y + jugador2.height//2 - 2, 10, 5)
                        balas_2.append(bala)
                        sonido_bala_disparo.play()
                        ultimo_disparo_jugador2 = tiempo_actual
                

            if event.type == jugador1_hit:
                vida_jugador1 -= 10
                sonido_bala_impacto.play()
                        
                        
            if event.type == jugador2_hit:
                vida_jugador2 -= 10
                sonido_bala_impacto.play()
        texto_ganador = ""
        
        if vida_jugador1 <= 0:
            texto_ganador = "JUGADOR 2 GANA"

        if vida_jugador2 <= 0:
            texto_ganador = "JUGADOR 1 GANA"

        if texto_ganador != "":
            dibujar_ganador(texto_ganador)
            run = False
                
        #musica_de_fondo()   
        keys_pressed = pygame.key.get_pressed()
        movimiento_nave_1(keys_pressed,jugador1)
        movimiento_nave_2(keys_pressed,jugador2)
        manejo_de_balas(balas_1,balas_2,jugador1,jugador2)
        dibujar_ventana(jugador1,jugador2,balas_1,balas_2,vida_jugador1,vida_jugador2)

        
    pygame.quit()



if __name__ == "__main__":
    main()
