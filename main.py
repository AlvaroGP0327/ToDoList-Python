import time
from itertools import count
from funcionalidades import *


def imprimir_cuadrado_con_texto(texto):
    longitud_texto = len(texto)
    ancho_cuadrado = longitud_texto + 4  # Ancho del cuadrado (texto + bordes)
    
    # Imprimir la línea superior del cuadrado
    print('*' * ancho_cuadrado)
    
    # Imprimir el contenido del cuadrado
    print(f'* {texto} *')
    
    # Imprimir la línea inferior del cuadrado
    print('*' * ancho_cuadrado)

def mostrar_menu() -> int:
    #Recibe una seleccion numerica y la retorna
    # La seleccion se utiliza para llamar funciones
    
    while True:
        imprimir_cuadrado_con_texto('TO DO LIST')
        print('Menu de aplicacion To Do List')
        print('1. Agregar Tarea')
        print('2. Editar Tarea')
        print('3. Marcar Tarea')
        print('4. Borrar Tarea')
        print('5. Listar Tareas')
        print('6. Salir')
        print('#@#@#@#@')
        try:
            seleccion = int(input('Seleccione opcion: '))
        except ValueError:
            print('Ingrese valor numerico del 1 al 6')
            time.sleep(3)
            continue #Indica que se regrese al inicio del ciclo
        if seleccion == 6:
            print('Saliendo de la aplicacion...')
            break
        elif seleccion > 6 or seleccion <= 0:
            print('Por favor ingrese una opcion valida...')
            time.sleep(2)
        else:
            print('redireccionando a la seleccion')
            match seleccion:
                case 1:
                    #Agregar Tarea
                    tarea = agregar()
                    escribir_en_db(tarea)
                    obtener_contenido(db)
                    time.sleep(3)
                case 2:
                    clave_editar = editar()
                    editar_en_db(clave_editar)
                case 3:
                    tarea = marcar()
                    tachar_en_db(tarea)
                    time.sleep(3)
                    #Pendiente remapear el db
                case 4:
                    clave = borrar()
                    borrar_tarea(clave)
                    obtener_contenido(db)
                case 5:
                    time.sleep(1)
                    listar(db)
                    time.sleep(3)

if __name__ == '__main__':
    mostrar_menu()

