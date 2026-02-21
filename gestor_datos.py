import json

def cargar():
    try:
        with open("datos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar(coleccion):
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(coleccion, archivo, indent=4)
    print("\nCambios guardados en datos.json")