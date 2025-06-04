"""Problema 2: Calculadora de Descuentos de Tienda
Situación Detallada:
Tienes una tienda en línea. Quieres incentivar compras grandes y fidelizar clientes. Tu estrategia comercial es:

Descuentos por volumen: Más compras = más descuento
Programa de membresía: Los miembros obtienen beneficios adicionales
Combinación de beneficios: Un miembro que compra mucho obtiene ambos descuentos

Lógica de Implementación Paso a Paso:
Paso 1: Determinar descuento base por monto
- ¿El monto es ≥ $200? → 15% de descuento (comprador VIP)
- Si no, ¿es ≥ $100? → 10% de descuento (comprador frecuente)  
- Si no, ¿es ≥ $50? → 5% de descuento (comprador casual)
- Si no → 0% de descuento

Paso 2: Verificar membresía
- ¿Es miembro? → +5% adicional al descuento base
- Si no → se mantiene el descuento base

Paso 3: Aplicar matemáticas
- Calcular dinero ahorrado: monto × (descuento_total ÷ 100)
- Calcular precio final: monto_original - dinero_ahorrado
"""

print("Muchisimas gracias por tu compra")

total_cliente= int(input("¿Cual fue el total de tu compra?: "))
membresia = input("Tienes Membresia?: ")

if((total_cliente>=200)&(membresia.upper=="SI")):
    total_con_descuento = total_cliente-(total_cliente*0.20) 
    print("Cliente VIP")
elif ((total_cliente>=200)&(membresia.upper!="SI")):
    total_con_descuento = total_cliente-(total_cliente*0.15)
    print("Cliente VIP")

elif ((total_cliente>=100)&(membresia.upper=="SI")):
    total_con_descuento = total_cliente-(total_cliente*0.15)
    print("Cliente frecuente")
elif ((total_cliente>=100)&(membresia.upper!="SI")):
    total_con_descuento = total_cliente-(total_cliente*0.10)
    print("Cliente frecuente")

elif ((total_cliente>=50)&(membresia.upper=="SI")):
    total_con_descuento = total_cliente-(total_cliente*0.10)
    print("Cliente normal")
elif ((total_cliente>=100)&(membresia.upper!="SI")):
    total_con_descuento = total_cliente-(total_cliente*0.05)
    print("Cliente VIP")

print(f"Su total habitual seria {total_cliente}, ahora con su descuento es {total_con_descuento}")


