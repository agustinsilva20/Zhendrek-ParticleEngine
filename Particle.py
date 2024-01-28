import pygame
from OneParticle import OneParticle

class Particle(pygame.sprite.Sprite):
    """def __init__(self,cantidad, x1:int, x2:int, y1:int, y2:int,
                 vx1:int, vx2:int, vy1:int, vy2:int,
                 life1, life2,
                 friccion, gravedad, rebote,
                 move_x1, move_x2, move_y1, move_y2,
                 spin1, spin2,
                 velocidad:int,
                 imagenes:list,
                 repeat:bool,
                 
                 colores,
                 screen
                 ):"""
    def __init__(self, dto, screen, player):
        
        # Creo el objeto de pygame
        super().__init__()
        self._layer = 101
        self.screen = screen
        self.player = player

        # Creo el rect
        self.image = pygame.Surface((1, 1))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        imagenes = []
        for elem in dto["particles"]:
            grafico = elem.copy()
            grafico.set_colorkey((0,0,0))
            self.colores = [dto["color1"], dto["color2"], dto["color3"], dto["color4"]]
            #self.imagen_pintada = self.set_color(grafico)
            self.imagen_pintada = self.set_color(self.colores, grafico)
            grafico = self.imagen_pintada.copy()

            imagenes.append(grafico)

        # Creo las particulas
        self.particulas = []
        for i in range(0, int(dto["cantidad"])):
            # Creo una nueva particula
            nueva_particula = OneParticle(int(dto["x1"]), int(dto["x2"]), int(dto["y1"]), int(dto["y2"]),
                 int(dto["vx1"]), int(dto["vx2"]), int(dto["vy1"]), int(dto["vy2"]),
                 int(dto["life1"]), int(dto["life2"]),
                 int(dto["friccion"]), int(dto["gravedad"]), int(dto["rebote"]),
                 int(dto["move_x1"]), int(dto["move_x2"]), int(dto["move_y1"]), int(dto["move_y2"]),
                 int(dto["spin1"]), int(dto["spin2"]),
                 int(dto["velocidad"]),
                 imagenes,
                 dto["repeat"],
                  self,
                  screen)
            # Agrego la particula a la lista
            self.particulas.append(nueva_particula)
        
        # Duraicon de las particulas
        if int(dto["life1"]) == -1:
            self.infinito = True
            
        else:
            self.infinito = False

        self.duracion = max(int(dto["life1"]), int(dto["life2"]))
        

        self.last_tick = pygame.time.get_ticks()
    
    def update(self):
        self.rect.x = 100
        self.rect.y = 100
        for elem in self.particulas:
            elem.update()
        
        if not self.infinito:
            time = pygame.time.get_ticks()
            delta = time - self.last_tick
            self.last_tick = time
            self.duracion -= delta
            if self.duracion <=0 and not self.infinito:
                self.kill()

    
    def kill(self):
        for elem in self.particulas:
            try:
                self.particulas.remove(elem)
                elem.kill()
            except:
                pass

        # Remuevo al player
        self.player.particle = None
        super().kill()

    
    
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        for elem in self.particulas:
            elem.draw()
    
    def set_color(self,colors, imagen):
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
    



        

