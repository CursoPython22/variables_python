# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese su primer nombre y luego su primer apellido
from pydoc import stripid


nombre = str(input('Ingrese por consola su primer nombre:'))

apellido = str(input('Ingrese por consola su primer apellido:'))

# Alumno:
# Imprima en pantalla su nombre y apellido
# utilizando las variables nombre y apellido

print("Tu nombre es :" , nombre , "y")
print("Tu apellido es :" , apellido)

# Crear una variable llamada nombre_apellido donde se 
# almacene el contenido de las variables nombre y apellido
# separando con un nespacio su nombre de su apellido

# nombre_apellido = .....

nombre_apellido = nombre + " "+apellido
print("Tu nombre y apellido son :" , nombre_apellido)

# Crear una variable llamada cantidad donde se
# almacene la cantidad de caracteres que posee la variable
# nombre_apellido utilizando la función len

# cantidad = len(....)

cantidad = len(nombre_apellido)

# Imprimir en pantalla la variable cantidad

print("Tu nombre tiene :" , cantidad , "caracteres inluyendo los espacios en blanco y")
cantidad = len(nombre_apellido.replace(' ',''))
print (cantidad , "sin espacios")
