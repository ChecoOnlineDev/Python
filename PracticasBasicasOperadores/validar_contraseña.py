"""
Problema 3: Verificador de Contraseñas
Situación Detallada:
Estás desarrollando el sistema de registro de una aplicación bancaria. La seguridad es crítica. Has investigado que las contraseñas débiles son la causa del 80% de los hackeos. Necesitas un filtro automático que rechace contraseñas inseguras ANTES de que se guarden en la base de datos.
Lógica de Implementación Detallada:
Requisitos mínimos definidos:
1. Al menos 8 caracteres (las contraseñas cortas se rompen fácil)
2. Al menos una mayúscula (aumenta complejidad exponencialmente)  
3. Al menos un número (previene contraseñas de solo letras)

Proceso de verificación:
Paso 1: Medir longitud
- len(contraseña) ≥ 8 → True/False

Paso 2: Buscar mayúscula
- Recorro cada carácter de la contraseña
- ¿Este carácter está entre 'A' y 'Z'? → Sí = encontré mayúscula
- Si termino el recorrido sin encontrar ninguna → False

Paso 3: Buscar número  
- Recorro cada carácter de la contraseña
- ¿Este carácter está entre '0' y '9'? → Sí = encontré número
- Si termino el recorrido sin encontrar ninguno → False

Paso 4: Decisión final
- ¿Cumple TODOS los requisitos? → Contraseña segura
- ¿Falla en alguno? → Contraseña rechazada
¿Por qué uso un bucle for en lugar de funciones predefinidas?

Con lógica básica: Tengo control total del proceso de verificación
Puedo expandir fácilmente (agregar verificación de símbolos especiales)
Es más educativo para entender la lógica

¿Por qué verifico con rangos de caracteres?

caracter >= 'A' and caracter <= 'Z': Verifica si está en el rango ASCII de mayúsculas
caracter >= '0' and caracter <= '9': Verifica si está en el rango ASCII de dígitos
Es más eficiente que verificar contra listas de caracteres
"""

contraseña = input("Por favor, ingresa tu contraseña: ")
longitud_valida = len(contraseña) >= 8
mayuscula_encontrada = False
numero_encontrado = False

# Verificar si la contraseña cumple con los requisitos
if not longitud_valida:
    print("Contraseña rechazada: debe tener al menos 8 caracteres.")    
for caracter in contraseña:
    if 'A' <= caracter <= 'Z':
        mayuscula_encontrada = True
    if '0' <= caracter <= '9':
        numero_encontrado = True 

if not mayuscula_encontrada:
    print("Contraseña rechazada: debe contener al menos una letra mayúscula.")
if not numero_encontrado:
    print("Contraseña rechazada: debe contener al menos un número.")
    
if longitud_valida and mayuscula_encontrada and numero_encontrado:
    print("Contraseña aceptada: cumple con todos los requisitos.")
else:
    print("Contraseña rechazada: no cumple con los requisitos de seguridad.")
# Fin del código


