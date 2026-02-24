import funciones
import gestor_datos

coleccion = gestor_datos.cargar()

def pedir_opcion(texto):
    try:
        return int(input(texto))
    except:
        return 0

def ejecucion_añadir():
    while True:
        print("\n===========================================\n        Añadir un Nuevo Elemento\n===========================================\n¿Qué tipo de elemento deseas añadir?\n1. Libro\n2. Película\n3. Música\n4. Regresar al Menú Principal\n===========================================")
        opc = pedir_opcion("Selecciona una opción (1-4): ")
        
        tipos = {1: "Libro", 2: "Película", 3: "Música"}
        if opc in tipos:
            item = {
                "tipo": tipos[opc],
                "titulo": input("Título: "),
                "autor": input("Autor/Director/Artista: "),
                "genero": input("Género: "),
                "valoracion": input("Valoración: ")
            }
            coleccion.append(item)
            print("\n Añadido con éxito.")
            funciones.pausa()
        elif opc == 4:
            break

def ejecucion_buscar():
    while True:
        print("\n===========================================\n        Buscar un Elemento\n===========================================\n¿Cómo deseas buscar?\n1. Buscar por Título\n2. Buscar por Autor/Director/Artista\n3. Buscar por Género\n4. Regresar al Menú Principal\n===========================================")
        opc = pedir_opcion("Selecciona una opción (1-4): ")
        campos = {1: "titulo", 2: "autor", 3: "genero"}
        if opc in campos:
            val = input("Texto a buscar: ")
            funciones.buscar(coleccion, campos[opc], val)
            funciones.pausa()
        elif opc == 4:
            break

def ejecucion_editar():
    while True:
        funciones.mostrar_formateado(coleccion)
        try:
            res = input("\nID a editar (o 's' para salir): ")
            if res.lower() == 's': break
            idx = int(res)
            
            print("\n===========================================\n        Editar un Elemento\n===========================================\n¿Qué tipo de cambio deseas realizar?\n1. Editar Título\n2. Editar Autor/Director/Artista\n3. Editar Género\n4. Editar Valoración\n5. Regresar al Menú Principal\n===========================================")
            opc = pedir_opcion("Selecciona una opción (1-5): ")
            campos = {1: "titulo", 2: "autor", 3: "genero", 4: "valoracion"}
            
            if opc in campos:
                coleccion[idx][campos[opc]] = input(f"Nuevo {campos[opc]}: ")
                print("\nEditado con exito.")
                funciones.pausa()
            elif opc == 5: break
        except:
            print("Error: ID no válido."); funciones.pausa()

def ejecucion_eliminar():
    while True:
        print("\n===========================================\n        Eliminar un Elemento\n===========================================\n¿Cómo deseas eliminar?\n1. Eliminar por Título\n2. Eliminar por Identificador Único\n3. Regresar al Menú Principal\n===========================================")
        opc = pedir_opcion("Selecciona una opción (1-3): ")
        if opc == 1:
            tit = input("Título a borrar: ")
            for e in coleccion[:]:
                if e['titulo'].lower() == tit.lower():
                    coleccion.remove(e)
            print("Proceso terminado."); funciones.pausa()
        elif opc == 2:
            funciones.mostrar_formateado(coleccion)
            idx = pedir_opcion("ID a eliminar: ")
            if 0 <= idx < len(coleccion): coleccion.pop(idx); print("Eliminado.")
            funciones.pausa()
        elif opc == 3: break

def ejecucion_categoria():
    while True:
        print("\n===========================================\n        Ver Elementos por Categoría\n===========================================\n¿Qué categoría deseas ver?\n1. Ver Libros\n2. Ver Películas\n3. Ver Música\n4. Regresar al Menú Principal\n===========================================")
        opc = pedir_opcion("Selecciona una opción (1-4): ")
        cats = {1: "Libro", 2: "Película", 3: "Música"}
        if opc in cats:
            funciones.mostrar_formateado(coleccion, cats[opc])
            funciones.pausa()
        elif opc == 4: break

def ejecucion_guardado():
    global coleccion
    while True:
        print("\n===========================================\n        Guardar y Cargar Colección\n===========================================\n¿Qué deseas hacer?\n1. Guardar la Colección Actual\n2. Cargar una Colección Guardada\n3. Regresar al Menú Principal\n===========================================")
        opc = pedir_opcion("Selecciona una opción (1-3): ")
        if opc == 1: gestor_datos.guardar(coleccion); funciones.pausa()
        elif opc == 2: coleccion = gestor_datos.cargar(); print("Cargado."); funciones.pausa()
        elif opc == 3: break

def main():
    while True:
        print("\n===========================================\n        Administrador de Colección\n===========================================\n1. Añadir un Nuevo Elemento\n2. Ver Todos los Elementos\n3. Buscar un Elemento\n4. Editar un Elemento\n5. Eliminar un Elemento\n6. Ver Elementos por Categoría\n7. Guardar y Cargar Colección\n8. Salir\n===========================================")
        opc = pedir_opcion("Selecciona una opción (1-8): ")
        
        if opc == 1: ejecucion_añadir()
        elif opc == 2: funciones.mostrar_formateado(coleccion); funciones.pausa()
        elif opc == 3: ejecucion_buscar()
        elif opc == 4: ejecucion_editar()
        elif opc == 5: ejecucion_eliminar()
        elif opc == 6: ejecucion_categoria()
        elif opc == 7: ejecucion_guardado()
        elif opc == 8: gestor_datos.guardar(coleccion); print("¡Adiós!"); break

if __name__ == "__main__":
    ejecucion_principal()
