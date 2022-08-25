# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

Cualquier duda con estos métodos pueden consultarla por el campus
'''

import string


print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio

# lower- Convertir texto a minúsculas en Python

nomb = 'BETY VANESA ARROBO ARCOS'
nomb= nomb.lower()
print(nomb)

# upper- Convertir texto a mayúsculas en Python
nomb1 = 'bety vanesa arrobo arcos'
nomb1 = nomb1.upper()
print(nomb1)

# capitalize Convertir solo la primera letra de un texto a mayúsculas


nombre='bety VANesa Arrobo Arcos'
print(f" ANTES DE CAPITALIZE(): {nombre}")
nombre=nombre.capitalize()
print(f" DESPUES  DE CAPITALIZE():{nombre}")




