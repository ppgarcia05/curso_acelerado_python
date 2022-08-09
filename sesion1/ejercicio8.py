'''
*********** Curso de programación acelerada en Python ************
Date 08-06-2022
File: sesion/ejercicio8.py
Autor: Jose Alfredo Garcia Gomez5
Action: calcular el sueldo mensual de un operador
'''
horas = float(input("Introduce tus horas de trabajo al dia: "))
horas = float(horas)
coste = float(input("Introduce lo que cobras por hora: "))
coste=float(coste)
pagodiario = (horas * coste)
pagosemana = (pagodiario*5)
pagomensual = (pagosemana*4)
print("Tu paga es", pagomensual)