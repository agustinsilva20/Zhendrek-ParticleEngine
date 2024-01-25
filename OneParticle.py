import random
import pygame
from pygame.math import Vector2
class OneParticle(pygame.sprite.Sprite):
    def __init__(self, x1:int, x2:int, y1:int, y2:int,
                 vx1:int, vx2:int, vy1:int, vy2:int,
                 life1, life2,
                 friccion, gravedad, rebote,
                 move_x1, move_x2, move_y1, move_y2,
                 spin1, spin2,
                 velocidad:int,
                 imagenes:list,
                 repeat:bool,
                 particula_padre,
                 screen):
        
        # Configuracion inicial pygame
        super().__init__()
        self._layer = 101
        self.particula_padre = particula_padre
        self.screen = screen

        # Guardo los valores
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.life1 = life1
        self.life2 = life2

        # Configuro la gravedad y estados de la particula
        self.friccion = friccion
        self.gravedad = gravedad
        self.rebote = rebote

        self.vx1 = vx1
        self.vx2 = vx2
        self.vy1 = vy1
        self.vy2 = vy2
        #self.vector_x = random.randint(vx1, vx2)
        #self.vector_y = random.randint(vy1, vy2)

        # Agrego unidades de desplazamiento de la particula
        
        if move_x1 != 0 or move_x2 != 0:
            self.move_x1 = move_x1
            self.move_x2 = move_x2
            self.isMoving_x = True
        else:
            self.isMoving_x = False
        
        if move_y1 != 0 or move_y2 != 0:
            self.move_y1 = move_y1
            self.move_y2 = move_y2
            self.isMoving_y = True
        else:
            self.isMoving_y = False
        
        # Rotacion
        if spin1 != 0 or spin2 != 0:
            self.spin1 = spin1
            self.spin2 = spin2
            self.isSpinning = True
        else:
            self.isSpinning = False
        
        # Velocidad
        self.velocidad = velocidad # Cada cuantos ms hago un tick

        # Infinite
        self.repeat = repeat

        # Imagen
        self.imagenes = imagenes
        """self.image = imagenes[0]
        self.rect = self.image.get_rect()
        self.image.set_alpha(200)"""

        """# Configuracion para el giro
        self.imagen_pintada = self.image.copy()
        self.offset = Vector2(0, 0)"""
        self.start_loop()
    
    def start_loop(self):
        # Calculo la posicion inicial tomando un numero aleatorio entre los limites
        self.x = random.randint(self.x1, self.x2)
        self.y = random.randint(self.y1, self.y2)

        # Calculo la duracion de la particula
        self.duracion = random.randint(self.life1, self.life2)

        # Configuro la direccion inicial de la particula
        self.vector_x = random.randint(self.vx1, self.vx2)
        self.vector_y = random.randint(self.vy1, self.vy2)

        # Seteo angulo de rotacion
        self.angulo = 0

        # Seteo los timer
        self.tiempo_inicio = pygame.time.get_ticks()
        self.last_tick = self.tiempo_inicio

        # Agarro la imagen
        rand_img = random.randint(0,len(self.imagenes)-1)
        self.image = self.imagenes[rand_img]
        self.rect = self.image.get_rect()
        self.image.set_alpha(200)

        # Configuracion para el giro
        self.imagen_pintada = self.image.copy()
        self.offset = Vector2(0, 0)



    
    def update(self):
        current_time = pygame.time.get_ticks()
        # Obtengo los ms que pasaron desde el ultimo tick
        delta = current_time - self.last_tick

        # Si aun no necesito un tick salgo
        if not delta >= self.velocidad:
            return
        
        # Le aplico la gravedad correspondiente
        self.vector_y += self.gravedad

        # Reboto en caso de llegar al suelo
        if self.y == 0:
            self.vector_y = - self.rebote
        
        # Aplico el giro
        if self.isSpinning:
            random_angle = random.randint(self.spin1, self.spin2)
            self.angulo = self.angulo + (random_angle)
            if self.angulo > 360:
                self.angulo = 0
            # HAGO GIRAR LA FOTO
            self.rotate()
        
        # Aplico movimiento
        if self.isMoving_x:
            movimiento = random.randint(self.move_x1, self.move_x2)
            self.vector_x = movimiento
        
        if self.isMoving_y:
            movimiento = random.randint(self.move_y1, self.move_y2)
            self.vector_y = movimiento
        
        # Actualizo la posicion
        self.x = self.x + (self.vector_x/self.friccion)
        self.y = self.y + (self.vector_y/self.friccion)

        print(f"vector_x: {self.vector_x}, {self.friccion}")

        # Descuento el tiempo de vida
        self.duracion = self.duracion - delta

        # Actualizo el timer
        self.last_tick = pygame.time.get_ticks()

        # Actualizo la posicion
        self.rect.x = self.particula_padre.rect.x + self.x
        self.rect.y = self.particula_padre.rect.y + self.y

        # Analizo que hacer con la particula
        if self.duracion <= 0:
            if self.repeat:
                # Reinicio la particula
                self.start_loop()
            else:
                self.kill()
            
    

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.imagen_pintada, -self.angulo, 1)
        print(self.angulo)
        offset_rotated = self.offset.rotate(self.angulo) #new
        self.rect = self.image.get_rect(center=self.particula_padre.rect.center+offset_rotated)
        #self.image.set_alpha(140)
        self.image.set_colorkey((0, 0, 0))
    
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        




    



    


        







         
