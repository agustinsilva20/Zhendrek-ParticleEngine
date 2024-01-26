import pygame

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert_alpha()
        
    def get_sprite(self, x, y, width, height):
        sprite= pygame.Surface([width, height], flags=pygame.SRCALPHA) # Este flag me permite laburar bien con los PNG, NECESITO per-pixel alphay no color key 
        sprite.blit(self.sheet, (0,0), ( x, y, width, height) )
        sprite.set_colorkey((0,0,0))
        return sprite

