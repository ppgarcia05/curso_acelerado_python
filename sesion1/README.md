# Sesion 1
---
Listado de ejercicios
* ejercicio1.py
Descripción: Asignación de Variables
```python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio1.py
Autor: Jose Alfredo Garcia Gomez
Action: asignación de variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = ['chiapas','campeche','veracruz']
productos = ['Cacao','Coco','Caña']
print(nombre_estado, " es un estado que ", )
print("con ",estados_cercanos[0], "colinda al sur", "y")
print("Tiene una superficie de ", superficie)
print("Tiene una poblacion de ", poblacion_total)
print("Su temperatura promedio es ", promedio_temperatura)
print("Uno de sus principal producto es el ",productos[0], "entre otros...")
```

---
* ejercicio2.py
Descripción: Asignación de Variables
```python
'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion/ejercicio2.py
Autor: Jose Alfredo Garcia Gomez
Action: superficie de un cuadrado
'''
lado=float(input("Ingrese la medida del lado del cuadrado:"))
lado=float(lado)
superficie=lado*lado
print("La superficie del cuadrado es")
print(superficie)
```

---
* ejercicio3.py
Descripción: Pago de trabajador
```python
'''
*********** Curso de programación acelerada en Python ************
Date 08-06-2022
File: sesion/ejercicio3.py
Autor: Jose Alfredo Garcia Gomez5
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
horas = float(horas)
coste = float(input("Introduce lo que cobras por hora: "))
coste=float(coste)
paga = horas * coste
print("Tu paga es", paga)
```

---
* ejercicio4.py
Descripción: indice de masa corporal peso en kg/ estatura mtrs cuadrados
```python
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
```

---
* ejercicio5.py
Descripción: Convierte grados Celcius a Farenheit
```python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio5.py
Autor: Jose Alfredo Garcia Gomez
Action: Convierte grados Celcius a Farenheit
'''
grados = float(input("Introduzca los grados Celsius "))
grados = float(grados)
faren = grados*1.8+32
print("La conversion a grados Farenheit es: ", faren)
```

---
* ejercicio6.py
Descripción: imprime capital obtenido de una inversión
```python
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
```

---
* ejercicio7.py
Descripción: Suma de los primeros números enteros
```python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio7.py
Autor: Jose Alfredo Garcia Gomez
Action: Suma de los primeros números enteros
'''
n = int(input("Introduce un número entero: "))
n =int(n)
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es "
+ str(suma))
```

---
* ejercicio8.py
Descripción: Suma de los primeros números enteros
```python
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
```
