from pathlib import Path , PureWindowsPath

carpeta =Path('C:/Users/elver/Documents/cursos/python federico/Dia6/archivo')
archivo = carpeta / 'archivo.txt'
print(archivo.read_text())

ruta_windows =PureWindowsPath(archivo)

if not archivo.exists():
    print('Este archivo no existe')
else:
    print('genial.existe')
    
print(ruta_windows)
