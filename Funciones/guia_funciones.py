# ==========================
# GUÍA DE FUNCIONES EN PYTHON
# ==========================

# 1. ¿Qué es una función?
# Una función es un bloque de código reutilizable que realiza una tarea específica.

# 2. Función básica sin parámetros ni retorno
def saludar():
    print("Hola mundo")

saludar()  # Salida: Hola mundo

# 3. Función con un parámetro
def saludar_persona(nombre):
    print(f"Hola {nombre}, bienvenido al mundo de las funciones!")

saludar_persona("Juan")  # Salida: Hola Juan, bienvenido al mundo de las funciones!

# 4. Función con varios parámetros y sin retorno
def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

sumar(5, 10)  # Salida: La suma de 5 y 10 es: 15

# 5. Función con retorno de valor
def resta(a, b):
    return a - b

resultado_resta = resta(10, 5)
print(f"La resta de 10 y 5 es: {resultado_resta}")  # Salida: La resta de 10 y 5 es: 5

# 6. Función con valor por defecto en parámetros
def saludar_con_titulo(nombre, titulo="Sr./Sra."):
    print(f"Hola {titulo} {nombre}")

saludar_con_titulo("Carlos")  # Salida: Hola Sr./Sra. Carlos
saludar_con_titulo("Ana", "Dra.")  # Salida: Hola Dra. Ana

# 7. Función que retorna múltiples valores
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones(8, 3)
print(f"Suma: {s}, Resta: {r}")  # Salida: Suma: 11, Resta: 5

# 8. Función con argumentos arbitrarios (*args)
def imprimir_nombres(*nombres):
    for nombre in nombres:
        print(f"Nombre: {nombre}")

imprimir_nombres("Ana", "Luis", "Pedro")

# 9. Función con argumentos clave arbitrarios (**kwargs)
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Lucía", edad=30, ciudad="Madrid")

# 10. Función anidada (función dentro de otra función)
def operacion_compleja(x, y):
    def suma(a, b):
        return a + b
    def multiplicacion(a, b):
        return a * b
    return suma(x, y), multiplicacion(x, y)

suma_res, mult_res = operacion_compleja(4, 5)
print(f"Suma: {suma_res}, Multiplicación: {mult_res}")

# 11. Función lambda (función anónima)
al_cuadrado = lambda x: x ** 2
print(al_cuadrado(6))  # Salida: 36

# 12. Función como argumento de otra función
def aplicar_funcion(func, valor):
    return func(valor)

print(aplicar_funcion(al_cuadrado, 7))  # Salida: 49

# 13. Función recursiva (factorial)
def factorial(n):
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Salida: 120

# 14. Función que maneja excepciones
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."

print(dividir(10, 2))  # Salida: 5.0
print(dividir(10, 0))  # Salida: Error: No se puede dividir por cero.

# 15. Función que utiliza variables globales
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)  # Salida: 2

# 16. Función con documentación (docstring)
def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Parámetros:
        radio (float): Radio del círculo.
    Retorna:
        float: Área del círculo.
    """
    from math import pi
    return pi * radio ** 2

print(area_circulo(3))  # Salida: 28.274333882308138

# 17. Función de orden superior (map, filter, reduce)
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # Salida: 15

# 18. Función decoradora básica
def mi_decorador(func):
    def nueva_funcion(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return nueva_funcion

@mi_decorador
def saluda():
    print("¡Hola desde una función decorada!")

saluda()

# Fin de la guía de funciones en Python.
