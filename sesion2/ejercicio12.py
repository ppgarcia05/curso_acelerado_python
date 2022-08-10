'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio12.py
Autor: Jose Alfredo Garcia Gomez
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes del año: "))
mes = int(mes)
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 11:
  print("El mes tiene 31 días.")
elif mes == 2: 
    print("El mes tiene 28 o 29 días.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes tiene 30 días.")
else:
    print("Mes no válido.")