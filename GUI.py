import tkinter as tk
from tkinter import ttk
import json
from Spritesheet import Spritesheet

def crear_particula(inputs, player):
    cantidad = inputs["entry_cantidad"].get()
    x1 = inputs["entry_x1"].get()
    x2 = inputs["entry_x2"].get()
    y1 = inputs["entry_y1"].get()
    y2 = inputs["entry_y2"].get()
    vx1 = inputs["entry_vx1"].get()
    vx2 = inputs["entry_vx2"].get()
    vy1 = inputs["entry_vy1"].get()
    vy2 = inputs["entry_vy2"].get()
    life1 = inputs["entry_life1"].get()
    life2 = inputs["entry_life2"].get()
    friccion = inputs["entry_friccion"].get()
    gravedad = inputs["entry_gravedad"].get()
    rebote = inputs["entry_rebote"].get()
    move_x1 = inputs["entry_movex1"].get()
    move_x2 = inputs["entry_movex2"].get()
    move_y1 = inputs["entry_movey1"].get()
    move_y2 = inputs["entry_movey2"].get()
    spin1 = inputs["entry_spin1"].get()
    spin2 = inputs["entry_spin2"].get()
    imagenes = inputs["entry_imagenes"].get()
    repeat = inputs["entry_repeat"].get()
    color1 = inputs["entry_color1"].get()
    color2 = inputs["entry_color2"].get()
    color3 = inputs["entry_color3"].get()
    color4 = inputs["entry_color4"].get()

    if repeat == 1 or repeat == "1":
        repeat = True
    else:
        repeat = False

    imagenes = imagenes.split(" ")
    imagenes = load_particles(imagenes)
    color1 = color1.split(" ")
    color2 = color2.split(" ")
    color3 = color3.split(" ")
    color4 = color4.split(" ")

    color1 = [int(x) for x in color1]
    color2= [int(x) for x in color2]
    color3 = [int(x) for x in color3]
    color4 = [int(x) for x in color4]


    objeto = {"id":1,
        "nombre": "",
        "cantidad" : cantidad,
        "x1" : x1,
        "x2" : x2,
        "y1" : y1,
        "y2" : y2,
        "vx1" : vx1,
        "vx2" : vx2,
        "vy1" : vy1,
        "vy2" : vy2,
        "life1" : life1,
        "life2" : life2,
        "friccion" : friccion,
        "gravedad" :gravedad,
        "rebote" : rebote,
        "move_x1" : move_x1,
        "move_x2" : move_x2,
        "move_y1" : move_y1,
        "move_y2" : move_y2,
        "spin1" : spin1,
        "spin2" : spin2,
        "velocidad": 15,
        "particles" : imagenes,
        "repeat" : repeat,
        "color1" : color1,
        "color2" : color2,
        "color3": color3,
        "color4" : color4           
        }
    
    player.crear_particula(objeto)



def escribir_textbox(objeto, inputs):
    entry = inputs["entry_cantidad"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["cantidad"])

    entry = inputs["entry_x1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["x1"])

    entry = inputs["entry_x2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["x2"])

    entry = inputs["entry_y1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["y1"])

    entry = inputs["entry_y2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["y2"])

    entry = inputs["entry_vx1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["vx1"])

    entry = inputs["entry_vx2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["vx2"])

    entry = inputs["entry_vy1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["vy1"])

    entry = inputs["entry_vy2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["vy2"])


    entry = inputs["entry_life1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["life1"])

    entry = inputs["entry_life2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["life2"])

    entry = inputs["entry_friccion"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["friccion"])

    entry = inputs["entry_gravedad"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["gravedad"])

    entry = inputs["entry_rebote"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["rebote"])

    entry = inputs["entry_movex1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["move_x1"])

    entry = inputs["entry_movex2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["move_x2"])

    entry = inputs["entry_movey1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["move_y1"])

    entry = inputs["entry_movey2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["move_y2"])

    entry = inputs["entry_spin1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["spin1"])

    entry = inputs["entry_spin2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["spin2"])

    entry = inputs["entry_velocidad"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["velocidad"])

    entry = inputs["entry_imagenes"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["imagenes"])

    entry = inputs["entry_repeat"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["repeat"])

    entry = inputs["entry_color1"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["color1"])

    entry = inputs["entry_color2"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["color2"])

    entry = inputs["entry_color3"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["color3"])

    entry = inputs["entry_color4"]
    entry.delete(0, tk.END)
    entry.insert(0, objeto["color4"])


# Función para manejar el evento de selección del cuadro de selección
def seleccionar_elemento(event, combo, elementos, diccionario, inputs):
    selected_element = combo.get()
    index = elementos.index(selected_element)
    objeto = diccionario[index+1]
    escribir_textbox(objeto, inputs)
    
    # Puedes realizar acciones según la selección

def bucle_tkinter(diccionario, player):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Formulario")

    elementos = []
    contador = 0
    for elem in diccionario:
        nombre = diccionario[elem]["nombre"]
        elementos.append(nombre)

    # Crear etiquetas y cuadros de texto para los campos
    label_cantidad = tk.Label(root, text="Cantidad:")
    entry_cantidad = tk.Entry(root)

    label_x1 = tk.Label(root, text="x1:")
    entry_x1 = tk.Entry(root)

    label_x2 = tk.Label(root, text="x2:")
    entry_x2 = tk.Entry(root)

    label_y1 = tk.Label(root, text="y1:")
    entry_y1 = tk.Entry(root)

    label_y2 = tk.Label(root, text="y2:")
    entry_y2 = tk.Entry(root)

    label_vx1 = tk.Label(root, text="vx1:")
    entry_vx1 = tk.Entry(root)

    label_vx2 = tk.Label(root, text="vx2:")
    entry_vx2 = tk.Entry(root)

    label_vy1 = tk.Label(root, text="vy1:")
    entry_vy1 = tk.Entry(root)

    label_vy2 = tk.Label(root, text="vy2:")
    entry_vy2 = tk.Entry(root)
    
    label_life1 = tk.Label(root, text="life1:")
    entry_life1 = tk.Entry(root)

    label_life2 = tk.Label(root, text="life2:")
    entry_life2 = tk.Entry(root)

    label_friccion = tk.Label(root, text="friccion:")
    entry_friccion = tk.Entry(root)

    label_gravedad = tk.Label(root, text="gravedad:")
    entry_gravedad = tk.Entry(root)

    label_rebote = tk.Label(root, text="rebote:")
    entry_rebote = tk.Entry(root)

    label_movex1 = tk.Label(root, text="move_x1:")
    entry_movex1 = tk.Entry(root)

    label_movex2 = tk.Label(root, text="move_x2:")
    entry_movex2 = tk.Entry(root)

    label_movey1 = tk.Label(root, text="move_y1:")
    entry_movey1 = tk.Entry(root)

    label_movey2 = tk.Label(root, text="move_y2:")
    entry_movey2 = tk.Entry(root)

    label_spin1 = tk.Label(root, text="spin1:")
    entry_spin1 = tk.Entry(root)

    label_spin2 = tk.Label(root, text="spin2:")
    entry_spin2 = tk.Entry(root)

    label_velocidad = tk.Label(root, text="velocidad:")
    entry_velocidad = tk.Entry(root)

    label_imagenes = tk.Label(root, text="imagenes:")
    entry_imagenes = tk.Entry(root)

    label_repeat = tk.Label(root, text="repeat:")
    entry_repeat = tk.Entry(root)

    label_color1 = tk.Label(root, text="color1:")
    entry_color1 = tk.Entry(root)

    label_color2 = tk.Label(root, text="color2:")
    entry_color2 = tk.Entry(root)

    label_color3 = tk.Label(root, text="color3:")
    entry_color3 = tk.Entry(root)

    label_color4= tk.Label(root, text="color4:")
    entry_color4 = tk.Entry(root)

    

    # Inputs
    inputs = {}
    inputs["entry_cantidad"] = entry_cantidad
    inputs["entry_x1"] = entry_x1
    inputs["entry_x2"] = entry_x2
    inputs["entry_y1"] = entry_y1
    inputs["entry_y2"] = entry_y2
    inputs["entry_vx1"] = entry_vx1
    inputs["entry_vx2"] = entry_vx2
    inputs["entry_vy1"] = entry_vy1
    inputs["entry_vy2"] = entry_vy2
    inputs["entry_life1"] = entry_life1
    inputs["entry_life2"] = entry_life2
    inputs["entry_friccion"] = entry_friccion
    inputs["entry_gravedad"] = entry_gravedad
    inputs["entry_rebote"] = entry_rebote
    inputs["entry_movex1"] = entry_movex1
    inputs["entry_movex2"] = entry_movex2
    inputs["entry_movey1"] = entry_movey1
    inputs["entry_movey2"] = entry_movey2
    inputs["entry_spin1"] = entry_spin1
    inputs["entry_spin2"] = entry_spin2
    inputs["entry_velocidad"] = entry_velocidad
    inputs["entry_imagenes"] = entry_imagenes
    inputs["entry_repeat"] = entry_repeat
    inputs["entry_color1"] = entry_color1
    inputs["entry_color2"] = entry_color2
    inputs["entry_color3"] = entry_color3
    inputs["entry_color4"] = entry_color4
    
    


    # Crear el cuadro de selección
    label_select = tk.Label(root, text="Selecciona un elemento:")
    combo = ttk.Combobox(root, values=elementos)
    combo.bind('<<ComboboxSelected>>', lambda event: seleccionar_elemento(event, combo, elementos, diccionario, inputs))


    boton = tk.Button(root, text="Visualizar", command=lambda:crear_particula(inputs, player))

    # Posicionar elementos en la ventana
    label_select.grid(row=0, column=0, pady=10)
    combo.grid(row=0, column=1, pady=10)

    label_cantidad.grid(row=1, column=0, pady=5)
    entry_cantidad.grid(row=1, column=1, pady=5)

    label_x1.grid(row=2, column=0, pady=5)
    entry_x1.grid(row=2, column=1, pady=5)

    label_x2.grid(row=3, column=0, pady=5)
    entry_x2.grid(row=3, column=1, pady=5)

    label_y1.grid(row=4, column=0, pady=5)
    entry_y1.grid(row=4, column=1, pady=5)

    label_y2.grid(row=5, column=0, pady=5)
    entry_y2.grid(row=5, column=1, pady=5)

    label_vx1.grid(row=6, column=0, pady=5)
    entry_vx1.grid(row=6, column=1, pady=5)

    label_vx2.grid(row=7, column=0, pady=5)
    entry_vx2.grid(row=7, column=1, pady=5)

    label_vy1.grid(row=8, column=0, pady=5)
    entry_vy1.grid(row=8, column=1, pady=5)

    label_vy2.grid(row=9, column=0, pady=5)
    entry_vy2.grid(row=9, column=1, pady=5)
    
    label_life1.grid(row=10, column=0, pady=5)
    entry_life1.grid(row=10, column=1, pady=5)

    label_life2.grid(row=11, column=0, pady=5)
    entry_life2.grid(row=11, column=1, pady=5)

    label_friccion.grid(row=12, column=0, pady=5)
    entry_friccion.grid(row=12, column=1, pady=5)

    label_gravedad.grid(row=13, column=0, pady=5)
    entry_gravedad.grid(row=13, column=1, pady=5)

    label_rebote.grid(row=14, column=0, pady=5)
    entry_rebote.grid(row=14, column=1, pady=5)

    label_movex1.grid(row=1, column=2, pady=5)
    entry_movex1.grid(row=1, column=3, pady=5)

    label_movex2.grid(row=2, column=2, pady=5)
    entry_movex2.grid(row=2, column=3, pady=5)

    label_movey1.grid(row=3, column=2, pady=5)
    entry_movey1.grid(row=3, column=3, pady=5)

    label_movey2.grid(row=4, column=2, pady=5)
    entry_movey2.grid(row=4, column=3, pady=5)

    label_spin1.grid(row=5, column=2, pady=5)
    entry_spin1.grid(row=5, column=3, pady=5)

    label_spin2.grid(row=6, column=2, pady=5)
    entry_spin2.grid(row=6, column=3, pady=5)

    label_velocidad.grid(row=7, column=2, pady=5)
    entry_velocidad.grid(row=7, column=3, pady=5)

    label_imagenes.grid(row=8, column=2, pady=5)
    entry_imagenes.grid(row=8, column=3, pady=5)

    label_repeat.grid(row=9, column=2, pady=5)
    entry_repeat.grid(row=9, column=3, pady=5)

    label_color1.grid(row=10, column=2, pady=5)
    entry_color1.grid(row=10, column=3, pady=5)

    label_color2.grid(row=11, column=2, pady=5)
    entry_color2.grid(row=11, column=3, pady=5)

    label_color3.grid(row=12, column=2, pady=5)
    entry_color3.grid(row=12, column=3, pady=5)

    label_color4.grid(row=13, column=2, pady=5)
    entry_color4.grid(row=13, column=3, pady=5)

    boton.grid(row = 14, column=3, pady=5)


    # Ejecutar el bucle principal de Tkinter
    root.mainloop()


def load_particles(imagenes):

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

   
        particles = []
        for elem in imagenes:
            particles.append(particulas_img[int(elem)])
 

    return particles