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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

from __future__ import division


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

# Calculadora
# Suma

print('Ingrese primer valor:')
num1=(float(input()))
print('Ingrese segundo valor:')
num2=(float(input()))
sum=num1+num2
print('La suma entre',num1, 'y', num2, 'es',sum)

# Resta

rest=num1-num2
print('La resta entre',num1, 'y',num2, 'es',rest)

# Multiplicacion

mult=num1*num2
print('La multiplicacion',num1,'y',num2, 'es', mult )

# Division

division=num1/num2
print('La division',num1,'y',num2, 'es',division )

# Exponete/Potencia

#exp=num1**num2
exp2=pow(num1,num2)
print('La potencia',num1,'y',num2, 'es', exp2 )







