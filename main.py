import pygame
import sys
import random

from Particle import Particle

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (255, 255,255)


# Configuración de la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zhendrek Particle Engine")

# Crear una instancia de la clase Particle
cantidad = 1
x1 = 0
x2 = 0
y1 = 0
y2 = 0
vx1 = 0
vx2 = 0
vy1 = 0
vy2 = 0
life1 = 1200
life2 = 1200
friccion = 10
gravedad =0
rebote = 0
move_x1 = -9
move_x2 = 9
move_y1 = -9
move_y2 = 9
spin1 = 0
spin2 = 0
velocidad= 20
imagen = ["1"]
repeat = True

particle = Particle(cantidad, x1, x2, y1, y2, vx1, vx2, vy1, vy2, life1, life2, friccion, gravedad, rebote, move_x1, move_x2, move_y1, move_y2, spin1, spin2, velocidad, imagen, repeat, screen)

# Bucle principal
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Actualizar la partícula
    particle.update()

    # Dibujo
    particle.draw()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(250)
