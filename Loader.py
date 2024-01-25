import json

def load_data():

    with open("./particles.json", 'r') as archivo:
        datos_json = json.load(archivo)
        diccionario = {}
        for elemento in datos_json:
            diccionario[int(elemento["id"])] = elemento
        return diccionario
            
