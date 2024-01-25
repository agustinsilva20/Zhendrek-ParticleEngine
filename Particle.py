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
    def __init__(self, dto, screen):
        
        # Creo el objeto de pygame
        super().__init__()
        self._layer = 101
        self.screen = screen


        # Creo el rect
        self.image = pygame.Surface((1, 1))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        """# Imagen
        grafico = pygame.image.load('./10090.bmp').convert_alpha()
        grafico = grafico.subsurface(pygame.Rect(480,0,32,32))
        grafico.set_colorkey((0, 0, 0))
        

        # Asigno el color
        self.colores = [dto["color1"], dto["color2"], dto["color3"], dto["color4"]]
        self.imagen_pintada = self.set_color(grafico)
        grafico = self.imagen_pintada.copy()
        #grafico.set_alpha(150)
        imagenes = []
        imagenes.append(grafico)"""

        imagenes = []
        for i in range(0, len(dto["imagenes"])):
            path = dto["imagenes"][i]
            recorte = dto["recortar_imagen"][i]
            grafico = pygame.image.load(f'./{path}').convert_alpha()
            grafico = grafico.subsurface(pygame.Rect(recorte[0],recorte[1],recorte[2],recorte[3]))
            grafico.set_colorkey((0, 0, 0))
            imagenes.append(grafico)

        
        imagenes.append(grafico)

        # Creo las particulas
        self.particulas = []
        for i in range(0, dto["cantidad"]):
            # Creo una nueva particula
            nueva_particula = OneParticle(dto["x1"], dto["x2"], dto["y1"], dto["y2"],
                 dto["vx1"], dto["vx2"], dto["vy1"], dto["vy2"],
                 dto["life1"], dto["life2"],
                 dto["friccion"], dto["gravedad"], dto["rebote"],
                 dto["move_x1"], dto["move_x2"], dto["move_y1"], dto["move_y2"],
                 dto["spin1"], dto["spin2"],
                 dto["velocidad"],
                 imagenes,
                 dto["repeat"],
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
    
    def set_color(self, imagen):
        color_left_bottom=self.colores[0]
        color_left_top=self.colores[1]
        color_right_bottom=self.colores[2]
        color_right_top=self.colores[3]

        # Crear una nueva superficie para la imagen con el mismo tamaño
        imagen_pintada = pygame.Surface(imagen.get_size(), pygame.SRCALPHA)
        imagen_pintada.blit(imagen, (0, 0))

        #Calculo los cuadrantes
        self.width = imagen.get_width()
        self.height = imagen.get_height()
        rect1 = pygame.Rect(0, 0, self.width // 2, self.height // 2)
        rect2 = pygame.Rect(self.width // 2, 0, self.width // 2, self.height // 2)
        rect3 = pygame.Rect(0, self.height // 2, self.width // 2, self.height // 2)
        rect4 = pygame.Rect(self.width // 2, self.height // 2, self.width // 2, self.height // 2)
        
        # Pinto por cuadrantes
        imagen_pintada.fill(color_left_bottom, rect = rect1, special_flags=pygame.BLEND_RGBA_MULT)
        imagen_pintada.fill(color_left_top, rect = rect2 , special_flags=pygame.BLEND_RGBA_MULT)
        imagen_pintada.fill(color_right_bottom, rect = rect3, special_flags=pygame.BLEND_RGBA_MULT)
        imagen_pintada.fill(color_right_top, rect = rect4, special_flags=pygame.BLEND_RGBA_MULT)

        return imagen_pintada
    
    """def set_color(self, imagen):
        # Crear una nueva superficie para la imagen con el mismo tamaño
        imagen_pintada = pygame.Surface(imagen.get_size(), pygame.SRCALPHA)

        # Calculo los cuadrantes
        self.width = imagen.get_width()
        self.height = imagen.get_height()
        rect1 = pygame.Rect(0, 0, self.width // 2, self.height // 2)
        rect2 = pygame.Rect(self.width // 2, 0, self.width // 2, self.height // 2)
        rect3 = pygame.Rect(0, self.height // 2, self.width // 2, self.height // 2)
        rect4 = pygame.Rect(self.width // 2, self.height // 2, self.width // 2, self.height // 2)

        # Pinto por cuadrantes con blending estándar
        imagen_pintada.blit(imagen, (0, 0))  # Copiar la imagen original
        imagen_pintada.fill(self.colores[0], rect=rect1, special_flags=pygame.BLEND_RGBA_ADD)
        imagen_pintada.fill(self.colores[1], rect=rect2, special_flags=pygame.BLEND_RGBA_ADD)
        imagen_pintada.fill(self.colores[2], rect=rect3, special_flags=pygame.BLEND_RGBA_ADD)
        imagen_pintada.fill(self.colores[3], rect=rect4, special_flags=pygame.BLEND_RGBA_ADD)
        imagen_pintada.set_colorkey((self.colores[0]))
        imagen_pintada.set_colorkey((self.colores[1]))
        imagen_pintada.set_colorkey((self.colores[2]))
        imagen_pintada.set_colorkey((self.colores[3]))
        return imagen_pintada"""

    """def set_color(self, imagen):
        # Crear una nueva superficie para la imagen con el mismo tamaño
        imagen_pintada = pygame.Surface(imagen.get_size(), pygame.SRCALPHA)

        # Calculo los cuadrantes
        self.width = imagen.get_width()
        self.height = imagen.get_height()
        rect1 = pygame.Rect(0, 0, self.width // 2, self.height // 2)
        rect2 = pygame.Rect(self.width // 2, 0, self.width // 2, self.height // 2)
        rect3 = pygame.Rect(0, self.height // 2, self.width // 2, self.height // 2)
        rect4 = pygame.Rect(self.width // 2, self.height // 2, self.width // 2, self.height // 2)

        # Pinto por cuadrantes aplicando color solo a píxeles no transparentes
        for rect, color in zip([rect1, rect2, rect3, rect4], self.colores):
            cuadrante = pygame.Surface(rect.size, pygame.SRCALPHA)
            cuadrante.fill(color)
            imagen_pintada.blit(cuadrante, rect)

        # Copiar la imagen original sobre los cuadrantes coloreados
        imagen_pintada.blit(imagen, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return imagen_pintada"""
    


        

