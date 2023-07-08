from itertools import count
import time

#Funcionalidades de la aplicacion


def agregar() ->str:
    #Recibe una tarea y la retorna
    tarea = input('Ingrese la tarea: ')
    return tarea
def editar() ->str:
    #Recibe un numero de tarea y lo retorna
    obtener_contenido(db)
    try:
        num_editar = int(input('Seleccione la tarea que desea editar: '))
    except ValueError:
        print('ingrese un numero de clave valido')
        return editar()
    size = tamano_db(db)
    if num_editar > size:
        print("Numero de tarea invalido")
        editar()
    else:
        return num_editar
def marcar():
    obtener_contenido(db)
    try:
        tarea = int(input('Seleccione la tarea que desea marcar: '))
    except ValueError:
        print('Ingrese un numero de clave valido')
        return marcar()
    size = tamano_db(db)
    if tarea > size:
        print('Numero de tarea invalido')
        marcar()
    return tarea

def borrar():
    #Pide un numero de registro para eliminar y lo retorna
    obtener_contenido(db)
    clave = int(input('Ingrese la tarea que desea eliminar'))
    return clave
def listar(db):
    #Mostar el estado actual del db
    print('LISTADO DE TAREAS')
    print('*********************')
    return obtener_contenido(db)

db = {}
contador = count(start=1)

def escribir_en_db(tarea):
    #Recibe una tarea y la guarda en db
    clave = next(contador)
    db[clave] = tarea
    print('Nueva tarea ingresada')
    return db

def editar_en_db(editar):
    #Recibe una clave, edita el valor y lo retorna
    valor_editado= input('Editar Tarea: ')
    db[editar] =  valor_editado
    print('Tarea editada con exito..')
    time.sleep(2)
    obtener_contenido(db)
    time.sleep(2)
    
def tachar_en_db(tarea):
    db[tarea] = f"{db[tarea]} \u2713 "
    print('Tarea Cumplida....Felicidades')
    time.sleep(2)
    obtener_contenido(db)

def ejecutar_en_db(opcion):
    del db[opcion]
    print('Tarea eliminada')
    time.sleep(2)

def obtener_contenido(db):
    #Desempacar el contenido del diccionario
    for clave, valor in db.items():
        print(clave, ':', valor)

def tamano_db(db):
    '''Validar las claves que mandan diccionario'''
    size = len(db)
    return size

def borrar_tarea(clave):
    del db[clave]
    print('Tarea eliminada')
    time.sleep(2)
    return db


def remapear_db():
    '''reorganizar la db despues de borrar'''
    pass