import pygame
from OneParticle import OneParticle
class Particle(pygame.sprite.Sprite):
    def __init__(self,cantidad, x1:int, x2:int, y1:int, y2:int,
                 vx1:int, vx2:int, vy1:int, vy2:int,
                 life1, life2,
                 friccion, gravedad, rebote,
                 move_x1, move_x2, move_y1, move_y2,
                 spin1, spin2,
                 velocidad:int,
                 imagenes:list,
                 repeat:bool,
                 screen
                 ):
        # Creo el objeto de pygame
        super().__init__()
        self._layer = 101
        self.screen = screen
        # Creo el rect
        self.image = pygame.Surface((1, 1))
        self.image.fill((255, 0, 0))
        #self.image.set_alpha(0)
        self.rect = self.image.get_rect()

        # Imagen
        grafico = pygame.image.load('./1.bmp').convert()
        grafico.set_colorkey((0, 0, 0))
        grafico.set_alpha(80)
        imagenes = []
        imagenes.append(grafico)

        # Creo las particulas
        self.particulas = []
        for i in range(0, cantidad):
            # Creo una nueva particula
            nueva_particula = OneParticle(x1, x2, y1, y2,
                 vx1, vx2, vy1, vy2,
                 life1, life2,
                 friccion, gravedad, rebote,
                 move_x1, move_x2, move_y1, move_y2,
                 spin1, spin2,
                 velocidad,
                 imagenes,
                 repeat,
                  self,
                  screen)
            # Agrego la particula a la lista
            self.particulas.append(nueva_particula)
    
    def update(self):
        self.rect.x = 100
        self.rect.y = 100
        for elem in self.particulas:
            elem.update()
        
    
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        for elem in self.particulas:
            elem.draw()

