from PIL import Image

def remove_background(input_path, output_path):
    # Abrir la imagen
    img = Image.open(input_path).convert("RGBA")

    # Obtener los datos de los píxeles
    data = img.getdata()

    # Crear una nueva lista de píxeles con transparencia
    new_data = []
    for item in data:
        # Eliminar los píxeles con el color de fondo (0, 162, 232)
        if item[:3] == (0, 162, 232):
            new_data.append((0, 0, 0, 0))  # Establecer el canal alfa a 0
        else:
            new_data.append(item)

    # Actualizar los datos de la imagen
    img.putdata(new_data)

    # Guardar la imagen con fondo transparente
    img.save(output_path, format="PNG")

if __name__ == "__main__":
    # Ruta de la imagen de entrada (debes proporcionar tu propia ruta)
    input_image_path = "./input.png"

    # Ruta de la imagen de salida
    output_image_path = "./output.png"

    # Eliminar el fondo y guardar la imagen
    remove_background(input_image_path, output_image_path)

    print(f"La imagen con fondo transparente se ha guardado en: {output_image_path}")
