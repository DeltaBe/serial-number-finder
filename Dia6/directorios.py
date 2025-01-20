import os
from pathlib import Path
carpeta =Path('C:/Users/elver/Documents/cursos/python federico/Dia6/archivo')
archivo = carpeta / 'archivo.txt'
mi = open(archivo)
print(mi.read())

# ruta = os.getcwd()
# ruta= 'C:\\Users\\elver\\Documents\\cursos\\python federico\\Dia6\\archivo'

# elemento = os.path.split(ruta)
# print(elemento)

# archivo = open('archivo.txt')
# print(archivo.read())

# otro =open('C:\\Users\\elver\\Documents\\cursos\\python federico\\Dia6\\archivo\\archivo.txt')
# print(otro.read())
