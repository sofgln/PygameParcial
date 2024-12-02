import pygame
from ventana import *
from naves import *
from movimiento import *

#fps

FPS=60






#función principal
def main():
    clock= pygame.time.Clock()
    run= True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
        keys_pressed = pygame.key.get_pressed()
        movimiento_nave_1(keys_pressed,jugador1)
        movimiento_nave_2(keys_pressed,jugador2)
        dibujar_ventana(jugador1,jugador2)

        
    pygame.quit()



if __name__ == "__main__":
    main()
