import tkinter as tk
from tkinter import ttk

# Lista de elementos para el cuadro de selección
elementos = ['Elemento1', 'Elemento2', 'Elemento3','Elemento1']

# Función para manejar el evento de selección del cuadro de selección
def seleccionar_elemento(event, combo, elementos, diccionario):
    selected_element = combo.get()
    index = elementos.index(selected_element)
    objeto = diccionario[index+1]
    print(objeto)
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


    # Crear el cuadro de selección
    label_select = tk.Label(root, text="Selecciona un elemento:")
    combo = ttk.Combobox(root, values=elementos)
    combo.bind('<<ComboboxSelected>>', lambda event: seleccionar_elemento(event, combo, elementos, diccionario))


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


    # ... Repite para otros campos

    # Ejecutar el bucle principal de Tkinter
    root.mainloop()
