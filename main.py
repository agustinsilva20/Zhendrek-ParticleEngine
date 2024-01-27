import pygame
import sys
from threading import Thread

from Particle import Particle
from ParticleLoader import load_particles

from GUI import bucle_tkinter

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (80, 80, 80)

# Configuración de la pantalla
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zhendrek Particle Engine")

# Crear una instancia de la clase Particle
# Cargo la config
diccionario = load_particles()

# Elijo la particula a mostrar
dto = diccionario[7]


class Player:
    def __init__(self) -> None:
        self.particle = Particle(dto, screen, self)

player = Player()

# Función para el bucle de particulas
def bucle_pygame(player):
    clock = pygame.time.Clock()

    player = player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpiar la pantalla
        screen.fill(WHITE)

        if player.particle:
            try:
                # Actualizar la partícula
                player.particle.update()

                # Dibujo
                player.particle.draw()
            except Exception as e:
                print(f"Error: {e}")

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de fotogramas
        clock.tick(250)





# Iniciar los hilos
thread_pygame = Thread(target=bucle_pygame, args=(player,))
thread_tkinter = Thread(target=bucle_tkinter, args=(diccionario, player,) )

thread_pygame.start()
thread_tkinter.start()

# Esperar a que ambos hilos finalicen (en este caso, nunca)
thread_pygame.join()
thread_tkinter.join()
