import pygame
import sys

from Particle import Particle
from Loader import load_data

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
"""cantidad = 6
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
imagen = ["apoca"]
repeat = True
color1 = (255, 124, 0)
color2 = (255, 124, 0)
color3 = (255, 124, 0)
color4 = (255, 124, 0)
colores = [color1,color2,color3,color4]"""

# Cargo la config
diccionario = load_data()

dto = diccionario[7]


#particle = Particle(cantidad, x1, x2, y1, y2, vx1, vx2, vy1, vy2, life1, life2, friccion, gravedad, rebote, move_x1, move_x2, move_y1, move_y2, spin1, spin2, velocidad, imagen, repeat, colores, screen)
particle = Particle(dto, screen)

# Bucle principal
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Actualizar la partícula
    particle.update()

    # Dibujo
    particle.draw()


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(250)
