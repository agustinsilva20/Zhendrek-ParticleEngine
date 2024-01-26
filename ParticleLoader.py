import json
from Spritesheet import Spritesheet

def load_data():

    with open("./particles.json", 'r') as archivo:
        datos_json = json.load(archivo)
        diccionario = {}
        for elemento in datos_json:
            diccionario[int(elemento["id"])] = elemento
        return diccionario
            
def load_particles():

    # Abro los sprite sheets
    spritesheets = {}

    with open("./Recursos/Particulas/images_index.json", 'r') as archivo:
        datos_json = json.load(archivo)
        for elem in datos_json:
            spritesheets[int(elem["id"])] = Spritesheet(elem["file"])
    
    # Realizo los recortes de cada sprite
    particulas_img = {}
    with open("./Recursos/Particulas/particle_assets.json", 'r') as archivo:
        datos_json = json.load(archivo)
        for elem in datos_json:
            # Obtengo el sprite sheet correspondiente
            spritesheet = spritesheets[int(elem["file"])]
            # Obtengo el recorte
            grafico = spritesheet.get_sprite(int(elem["x"]), int(elem["y"]), int(elem["width"]), int(elem["height"]))
            # Almaceno el recorte
            particulas_img[int(elem["id"])] = grafico

    # Inicio un diccionario donde voy a almacenar la informacion de cada particula
    diccionario = {}
    with open("./Recursos/Particulas/particles.json", 'r') as archivo:
        datos_json = json.load(archivo)
        for elemento in datos_json:

            # Agrego las imagenes
            particles = []
            for elem in elemento["imagenes"]:
                particles.append(particulas_img[int(elem)])
            elemento["particles"] = particles
            # Almaceno cada informacion
            diccionario[int(elemento["id"])] = elemento

    return diccionario