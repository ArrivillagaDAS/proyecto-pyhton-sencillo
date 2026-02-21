def pausa():
    input("\nPresiona Enter para continuar...")

def mostrar_formateado(lista, filtro_tipo=None):
    print("\n--- Listado de Elementos ---")
    encontrado = False
    for i, e in enumerate(lista):
        if filtro_tipo is None or e['tipo'] == filtro_tipo:
            print(f"ID: {i} | [{e['tipo']}] {e['titulo']} - {e['autor']} ({e['genero']})")
            encontrado = True
    if not encontrado:
        print("No hay elementos registrados.")

def buscar(lista, campo, valor):
    print("\n--- Resultados ---")
    encontrado = False
    for e in lista:
        if valor.lower() in str(e[campo]).lower():
            print(f"[{e['tipo']}] {e['titulo']} - {e['autor']}")
            encontrado = True
    if not encontrado:
        print("No se encontraron coincidencias.")