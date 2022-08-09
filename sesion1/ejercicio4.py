'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio4.py
Autor: Jose Alfredo Garcia Gomez
Action: indice de masa corporal peso en kg/ estatura mtrs cuadrados
'''
peso = float(input("¿Cuál es tu peso en kg? "))
peso = float(peso)
estatura = float(input("¿Cuál es tu estatura en metros? "))
estatura = float(estatura)
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))