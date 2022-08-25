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

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''
print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio

print('Ingrese el primer nombre')
nom1=str(input())
print('Ingrese el segundo nombre')
nom2=str(input())
print('Ingrese el apellido paterno')
apel1=str(input())
print('Ingrese el apellido materno')
apel2=str(input())
print('Ingrese DNI')
ced=int(input())
print('Ingrese edad')
edad=int(input())
print('Ingrese altura')
altura=float(input())

print('Nombre Apellido:',nom1,'', apel1, 'DNI:',ced )
print('Nombre completo:',nom1,'',nom2,'',apel1,'',apel2, 'EDAD ES:' ,edad, 'LA ALTURA ES:', altura)