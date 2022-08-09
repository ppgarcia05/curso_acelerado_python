'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio6.py
Autor: Jose Alfredo Garcia Gomez
Action: imprime capital obtenido de una inversión
'''
cantidad =float(input("¿Cantidad a invertir? "))
cantidad =float(cantidad)
interes = float(input("¿Interés porcentual anual? " ))
interes =float(interes)
años = int(input("¿Años?"))
años = int(años)
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))