# Sesion 2
---
Listado de ejercicios
* ejercicio9.py
Descripción: detecta numero negativos
```python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio9.py
Autor: Jose Alfredo Garcia Gomez
Action: detecta numero negativos
'''t(numero)
if numero != 0:
  if numero > 0:
    print(f"El numero {numero} es positivo"
numero = int(input("Escriba un número: "))
numero = in)
  else:
      print(f"El numero {numero} es negativo")
else:
  print("El número dado es cero")
```

---
* ejercicio10.py
Descripción: Compara contraseña
```python
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
  ```
  
 ---
* ejercicio11.py
Descripción: numero par o impar
```python
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
```

 ---
* ejercicio12.py
Descripción: estructura condicional anidada
```python
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
```

---
* ejercicio13.py
Descripción: estructura condicional anidada
```python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio13.py
Autor: Jose Alfredo Garcia Gomez
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes de año: "))
if 1 <= mes <= 12:
 print("Se ha introducido un mes válido.")
else:
 print("El mes es incorrecto. Por defecto se elige Enero.")
 mes = 1
print("Se utilizará mes", mes)
```
