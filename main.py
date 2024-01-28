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
        self.particle = None
        self.x = 200
        self.y = 200
    
    def crear_particula(self, objeto):
        self.particle = None
        self.particle = Particle(objeto, screen, self)

player = Player()

def bucle_pygame(player):
    clock = pygame.time.Clock()
    
    player = player

    thread_tkinter = Thread(target=bucle_tkinter, args=(diccionario, player,) )
    thread_tkinter.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpiar la pantalla
        screen.fill(BLACK)

        if player.particle:
            try:

                player.particle.update()

                player.particle.draw()
            except Exception as e:
                pass

        pygame.display.flip()

        clock.tick(250)




bucle_pygame(player)

#


