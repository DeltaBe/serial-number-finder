from pathlib import Path
from os import system

#este metodo lee las recetas dentro de una categoria especifica
def leer_categoria():
    #accedo a la ruta principal de mis recetas
    ruta_base = Path('C:/Users/elver/Documents/cursos/python federico/Dia6/Recetas')
    #iteramos sobre cada carpeta dentro de recetas ya que iterdir nos permite iterar los elementos en el directorio especificado ademas utilizamos is_dir para considerar solo esas carpetas
    subcarpetas = [carpeta for carpeta in ruta_base.iterdir() if carpeta.is_dir()]
    # for carpeta in ruta_base.iterdir(): 
    #     print(carpeta)
    
    #enumeramos las carpetas con el metodo enumerate ademas de que con carpeta.name hacemos que solo nos muestre ek nombre de las carpetas y no toda la direccion
    for i , carpeta in enumerate(subcarpetas):
        print(f'{i}.{carpeta.name}')
    salir = True
    #el metodo while para iterar cuantas veces queramos en las carpetas
    while salir:
             
             #le pedimos que eliga una opcion de las que se mostraron en el metodo enumerate 
             
            opcion = int(input('Digita que a que carpeta deseas ingresar si deseas salir presiona -99 '))
            # verificamos si la opcion es mayor o igual a 0 pero menor a la longitud de carpetas
            if 0<= opcion < len(subcarpetas):
                #agregamos una nueva variable que almacenara la direccion de donde se encuentra la carpeta que seleccionamos
                carpeta_seleccionada = subcarpetas[opcion]
                print(f'Has seleccionado la carpeta:{carpeta_seleccionada}')
                #iteramos sobre todos los archivos que existan en ese momento gracias a la ayuda de glob() ya que nos permite hacer una busque sobre que tipo de archivos me gustaria iterar
                for i in carpeta_seleccionada.glob('*.txt'):
                    print(i.name)
            elif opcion == -99:
                salir = False
                
   
            
            
            
            
        
    

def crear_receta():
    
    ruta_base = Path('C:/Users/elver/Documents/cursos/python federico/Dia6/Recetas')
    #iteramos sobre cada carpeta dentro de recetas ya que iterdir nos permite iterar los elementos en el directorio especificado ademas utilizamos is_dir para considerar solo esas carpetas
    subcarpetas = [carpeta for carpeta in ruta_base.iterdir() if carpeta.is_dir()]
    # for carpeta in ruta_base.iterdir(): 
    #     print(carpeta)
    
    #enumeramos las carpetas con el metodo enumerate ademas de que con carpeta.name hacemos que solo nos muestre ek nombre de las carpetas y no toda la direccion
    for i , carpeta in enumerate(subcarpetas):
        print(f'{i}.{carpeta.name}')
    salir = True
    #el metodo while para iterar cuantas veces queramos en las carpetas
    while salir:
             
             #le pedimos que eliga una opcion de las que se mostraron en el metodo enumerate 
             
            opcion = int(input('Digita que a que carpeta deseas ingresar para colocar la receta si deseas salir presiona -99 '))
            # verificamos si la opcion es mayor o igual a 0 pero menor a la longitud de carpetas
            if 0<= opcion < len(subcarpetas):
                #agregamos una nueva variable que almacenara la direccion de donde se encuentra la carpeta que seleccionamos
                carpeta_seleccionada = subcarpetas[opcion]
                print(f'Has seleccionado la carpeta:{carpeta_seleccionada}')
                #le pedimos al usuario que ingrese el nombre del archivo luego le unimos las sigles .txt con join
                nombre_archivo = input('Escribe el nombre de tu archivo: ')
                nombre_archivo = f'{nombre_archivo}.txt'
                #abrimos el archivo en el directorio en el que escoogimos y escribimos algo
                abrir_nuevo_archivo = open(Path(carpeta_seleccionada)/nombre_archivo,'a')
                escribir = input('Escribe algo en el archivo: ')                
                abrir_nuevo_archivo.write(escribir)
                #cerramos el archivo para luego volverlo abrir en lectura 
                abrir_nuevo_archivo.close()
                abrir_nuevo_archivo = open(Path(carpeta_seleccionada)/nombre_archivo,'r')
                print(abrir_nuevo_archivo.read())
                
                for i in carpeta_seleccionada.glob('*.txt'):
                    print(i.name)
                
            elif opcion == -99:
                salir = False
    
                

def crear_categoria():
    ruta_base = Path('C:/Users/elver/Documents/cursos/python federico/Dia6/Recetas')
    # escribimos el nombre de la carpeta a crear
    nombre_carpeta = input('Escribe el nombre de la categoria a crear: ')
    #unimos con el directorio base para que se cree en donde queremos
    carpeta_creada = ruta_base / nombre_carpeta
    #utilizamos el metodo mkdir para crear la nueva carpeta
    carpeta_creada.mkdir(parents=True,exist_ok=True)
     #iteramos sobre cada carpeta dentro de recetas ya que iterdir nos permite iterar los elementos en el directorio especificado ademas utilizamos is_dir para considerar solo esas carpetas
    subcarpetas = [carpeta for carpeta in ruta_base.iterdir() if carpeta.is_dir()]
    # for carpeta in ruta_base.iterdir(): 
    #     print(carpeta)
    
    #enumeramos las carpetas con el metodo enumerate ademas de que con carpeta.name hacemos que solo nos muestre ek nombre de las carpetas y no toda la direccion
    for i , carpeta in enumerate(subcarpetas):
        print(f'{i}.{carpeta.name}')
    
   
        
  
  
        
def eliminar_receta():
    
    ruta_base = Path('C:/Users/elver/Documents/cursos/python federico/Dia6/Recetas')
    #iteramos sobre cada carpeta dentro de recetas ya que iterdir nos permite iterar los elementos en el directorio especificado ademas utilizamos is_dir para considerar solo esas carpetas
    subcarpetas = [carpeta for carpeta in ruta_base.iterdir() if carpeta.is_dir()]
    # for carpeta in ruta_base.iterdir(): 
    #     print(carpeta)
    
    #enumeramos las carpetas con el metodo enumerate ademas de que con carpeta.name hacemos que solo nos muestre ek nombre de las carpetas y no toda la direccion
    for i , carpeta in enumerate(subcarpetas):
        print(f'{i}.{carpeta.name}')
    salir = True
    #el metodo while para iterar cuantas veces queramos en las carpetas
    while salir:
             
             #le pedimos que eliga una opcion de las que se mostraron en el metodo enumerate 
             
            opcion = int(input('Digita que a que carpeta deseas ingresar para eliminar la receta si deseas salir presiona -99 '))
            # verificamos si la opcion es mayor o igual a 0 pero menor a la longitud de carpetas
            if 0<= opcion < len(subcarpetas):
                #agregamos una nueva variable que almacenara la direccion de donde se encuentra la carpeta que seleccionamos
                carpeta_seleccionada = subcarpetas[opcion]
                print(f'Has seleccionado la carpeta:{carpeta_seleccionada}')
                #le pedimos al usuario que ingrese el nombre del archivo luego le unimos las sigles .txt con join
                nombre_archivo = input('Escribe el nombre de tu archivo a eliminar: ')
                nombre_archivo = f'{nombre_archivo}.txt'
                elimiar_archivo = carpeta_seleccionada/nombre_archivo
                if elimiar_archivo.exists():
                    elimiar_archivo.unlink()
                else:
                    print('receta no encontrada')
                    for i in carpeta_seleccionada.glob('*.txt'):
                       print(i.name)
            
            elif opcion == -99:
                salir = False
   
                
                        
                        
                  
                

def eliminar_categoria():
    ruta_base = Path('C:/Users/elver/Documents/cursos/python federico/Dia6/Recetas')
    # escribimos el nombre de la carpeta a crear
    nombre_carpeta = input('Escribe el nombre de la categoria a eliminar: ')
    #unimos con el directorio base para que se cree en donde queremos
    carpeta_eliminada = ruta_base / nombre_carpeta
    #utilizamos el metodo mkdir para crear la nueva carpeta
    if carpeta_eliminada.exists():
        
        carpeta_eliminada.rmdir()
        
    else:
        print('carpeta no encontrada')
     #iteramos sobre cada carpeta dentro de recetas ya que iterdir nos permite iterar los elementos en el directorio especificado ademas utilizamos is_dir para considerar solo esas carpetas
    subcarpetas = [carpeta for carpeta in ruta_base.iterdir() if carpeta.is_dir()]
    # for carpeta in ruta_base.iterdir(): 
    #     print(carpeta)
    
    #enumeramos las carpetas con el metodo enumerate ademas de que con carpeta.name hacemos que solo nos muestre ek nombre de las carpetas y no toda la direccion
    for i , carpeta in enumerate(subcarpetas):
        print(f'{i}.{carpeta.name}')
    
    



while True :
    print(''' Bienvenidos al catologo de recetario
               elige una opcion 
          1. leer categorias existentes
          2. crear tu propia receta
          3. crear tu categoria de recetas
          4. elimina una receta existente
          5. eliminar una categoria \n''')
    opcion = int(input('Por favor digite su opcion: '))
    
    if opcion == 1:
        leer_categoria()
        print('\n')
        system('cls')    
    elif opcion == 2:
        crear_receta()
        print('\n')
        system('cls')    
    
    elif opcion == 3:
        crear_categoria()
        print('\n')
    elif opcion == 4:
        eliminar_receta()
        print('\n')
        system('cls')    
    elif opcion == 5:
        eliminar_categoria()
        print('\n')
    elif opcion == 6:
        system('cls')  
        print('hasta la proxima')  
        break
    
    
    

