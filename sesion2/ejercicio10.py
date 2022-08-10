'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio10.py
Autor: Jose Alfredo Garcia Gomez
Action: compara contraseña
'''
contrasena = "cunuco"
valor = str(input("Escriba la  contraseña correcta: "))
valor = str(valor)
if valor == contrasena:
  print("Contraseña correcta")
else:
  print("Contraseña incorrecta")