'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio11.py
Autor: Jose Alfredo Garcia Gomez
Action: numero par o impar
'''
n = int(input("Introduce un número entero: "))
n = int(n)
if n % 2 == 0:
 print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")