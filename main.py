import pygame
import sys

from Particle import Particle
from ParticleLoader import load_particles

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0,0,0)
WHITE = (80,80,80)


# Configuración de la pantalla
screen_width, screen_height = 800, 600
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


# Bucle principal
clock = pygame.time.Clock()
player = Player()
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
        except:
            pass


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(250)
