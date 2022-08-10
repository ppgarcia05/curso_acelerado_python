'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio8.py
Autor: ..............
Action: detecta numero negativos
'''
numero = int(input("Escriba un número: "))
numero = int(numero)
if numero != 0:
  if numero > 0:
    print(f"El numero {numero} es positivo")
  else:
      print(f"El numero {numero} es negativo")
else:
  print("El número dado es cero")