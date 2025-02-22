import os 
from pathlib import Path
import re
from datetime import datetime
import time
import math
#Buscador de numeros de series
def buscando_ruta():
    #donde se guardara todos  los retornos de la funcion abriendo archivo
    tuplas = []
    #path.cwd nos manda la locacion bien localizada donde nuestro archivo se esta ejecutando
    ruta = Path.cwd()/'Dia9'/'proyectoDia9'/'Proyecto+Dia+9'/'Mi_Gran_Directorio'
    #ciclo en el cual recorreremos todas las carpetas y archivos dentro de la ruta deseada
    for carpeta,subcarpeta,archivo in os.walk(ruta):
        # print(f' en la carpeta: {carpeta}')
        # print(f'las sub carpetas son:')
        # for sub in subcarpeta:
        #     # print(f'\t{sub}')
        #     print()
        # print('los archivos son:')
        for arch in archivo:
            # si existe el archivo con terminacion .txt se ejecutara esto
            if arch.endswith('.txt'):
                #variable en la cual se guardara el resultado 
                coincidiencias=arbriendo_archivo(carpeta,arch)
                # print(f'\t{arch}')
                #se agrega a la lista tuplas
                tuplas.append(coincidiencias)
        
             
        print('\n')
    return tuplas
    

def arbriendo_archivo(carpeta,archivo):
    #abrimos la ruta del archivo
     abrir=open(f'{carpeta}\\{archivo}','r')
     #leemos el archivo
     contenido = abrir.read()
     #la partitura es decir el formato en el que buscaremos
     pattern = r"N[a-zA-Z]{3}-\d{5}"
     #si existe se guardara en esta variable 
     matches  = re.findall(pattern, contenido)
    #  print(matches)
     #retornamos tanto la serie como el archivo
     return matches,archivo

    
#imprimimos en el formato deseado
def imprimir(tuplas):
    # Obtener la fecha actual en formato dd/mm/aa
    fecha_actual = datetime.now().strftime("%d/%m/%y")
    print("Fecha actual:", fecha_actual)
    print('-'*50)
    print('Archivo'+' '*10 + 'N-Serie')
    print('-'*50)
   #desempaquetamos cada tupla 
    for serie,archivo in tuplas:
         print(f'{archivo}    {serie}')
    
    print(f'Numeros encontrados: {len(tuplas)}')
    print('-'*50)



#haciendo que funcionen las funciones
inicio = time.time()
devolvio = buscando_ruta()
tuplas_validas = [t for t in devolvio if t[0]]
imprimir(tuplas_validas)
final = time.time()
resultado = math.ceil(final - inicio)
print(f'Duracion de la busqueda: {resultado} Segs')
print('-'*50)



    

                

    



