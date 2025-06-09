def saludar():
    print("hola mundo")


saludar();

#ahora haremos una funcion que reciba un parametro y lo imprima
def saludar_persona(nombre):
    print(f"Hola {nombre}, bienvenido al mundo de las funciones!")

# Llamamos a la función con un argumento
saludar_persona("Juan")

# Ahora crearemos una funcion que reciba dos parametros y los sume
def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
# Llamamos a la función con dos argumentos
sumar(5, 10)    

# Ahora crearemos una funcion que reciba dos parametros y los reste
def restar(a, b):
    resultado = a - b
    print(f"La resta de {a} y {b} es: {resultado}")
# Llamamos a la función con dos argumentos
restar(10, 5)

# Ahora crearemos una funcion que reciba dos parametros y los multiplique
def multiplicar(a, b):
    resultado = a * b
    print(f"La multiplicación de {a} y {b} es: {resultado}")            
    
# Llamamos a la función con dos argumentos
multiplicar(5, 10)
# Ahora crearemos una funcion que reciba dos parametros y los divida
def dividir(a, b):
    if b != 0:
        resultado = a / b
        print(f"La división de {a} entre {b} es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")

# Llamamos a la función con dos argumentos
dividir(10, 2)

# Ahora crearemos una funcion que reciba dos parametros y los divida
def potencia(base, exponente):
    resultado = base ** exponente
    print(f"{base} elevado a la {exponente} es: {resultado}")
    
# Llamamos a la función con dos argumentos
potencia(2, 3)

# Ahora crearemos una funcion que reciba dos parametros y los divida
def raiz_cuadrada(numero):
    if numero >= 0:
        resultado = numero ** 0.5
        print(f"La raíz cuadrada de {numero} es: {resultado}")
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")  
        
# Llamamos a la función con un argumento
raiz_cuadrada(16)  

# Ahora crearemos una funcion que reciba dos parametros y los divida
def factorial(numero):
    if numero < 0:
        print("Error: No se puede calcular el factorial de un número negativo.")
        return
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        print(f"El factorial de {numero} es: {resultado}")

# Llamamos a la función con un argumento
factorial(5)


