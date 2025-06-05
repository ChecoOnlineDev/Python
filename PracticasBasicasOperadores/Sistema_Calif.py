"""
Problema 1: Sistema de Calificaciones
Situación: Un profesor necesita convertir calificaciones numéricas a letras.
"""
calificacion = int(input("Dime tu calificacion: "))
print("Holaa")

if calificacion>=9:
    letra ="A"
    print("Excelente")
elif calificacion>=8:
    letra = "B"
    print("Bastante bien")
elif calificacion>=7:
    letra = "C"
    print("Bien")
elif calificacion>=6:
    letra ="D"
    print("Pudo ser mejor")
else :
    letra = "F"
    print("Reprobado")
print(letra)