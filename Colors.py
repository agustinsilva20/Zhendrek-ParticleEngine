import pygame

"""# Here something to play with. 
def create_overlay(colors, size):
    overlay = pygame.Surface((2, 2), pygame.SRCALPHA)
    overlay.set_at((0, 0), colors[0])
    overlay.set_at((1, 0), colors[1])
    overlay.set_at((0, 1), colors[2])
    overlay.set_at((1, 1), colors[3])
    return pygame.transform.smoothscale(overlay, size)

rect = image.get_rect()
overlay = create_overlay(('orange', 'purple', 'yellow', 'red'), rect.size)
image.blit(overlay, (0, 0), None, pygame.BLEND_MULT)"""

# Lets you do same size blocks. 2x2, 3x3, 4x4, so on.
def create_overlay(colors, imagen):
    size = imagen.get_size()
    root = int(len(colors) ** 0.5)
    overlay = pygame.Surface((root, root), pygame.SRCALPHA)
    for y in range(root):
        for x in range(root):
            overlay.set_at((x, y), colors[x + y * root])

    colored_image = pygame.transform.smoothscale(overlay, size)

    # Hago una copia de la imagen origina
    final_image = imagen.copy()

    # Pinto la imagen
    final_image.blit(colored_image, (0, 0), special_flags = pygame.BLEND_MULT)

    return final_image

