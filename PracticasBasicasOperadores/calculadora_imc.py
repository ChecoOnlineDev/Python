"""
Problema 4: Calculadora de IMC y Recomendaciones
Situación Detallada:
Trabajas para una app de salud. Los usuarios ingresan su peso y altura, y necesitas darles información médicamente precisa sobre su estado de salud, usando los estándares de la Organización Mundial de la Salud (OMS).
Lógica de Implementación Médica:
Fórmula del IMC: peso(kg) ÷ altura(m)²

Clasificaciones oficiales de la OMS:
- Menos de 18.5: Bajo peso (riesgo de desnutrición)
- 18.5 a 24.9: Peso normal (saludable)  
- 25.0 a 29.9: Sobrepeso (riesgo cardiovascular moderado)
- 30.0 o más: Obesidad (riesgo cardiovascular alto)

Mi proceso de decisión:
1. Calcular IMC con la fórmula exacta
2. Comparar contra los rangos médicos oficiales
3. Asignar categoría correspondiente  
4. Dar recomendación apropiada (no diagnóstico médico)
¿Por qué uso < en lugar de <= para los límites?

IMC de exactamente 18.5 debe estar en "peso normal", no en "bajo peso"
IMC de exactamente 25.0 debe estar en "sobrepeso", no en "peso normal"
Los rangos médicos son: [18.5, 25), [25, 30), [30, ∞)

¿Por qué incluyo recomendaciones?

Un número sin contexto no es útil para el usuario
Las recomendaciones guían la acción sin dar consejos médicos específicos
Siempre sugiero consultar profesionales para casos que requieren atención

Ejemplo de cálculo:

Persona: 70 kg, 1.75 m
IMC = 70 ÷ (1.75 × 1.75) = 70 ÷ 3.0625 = 22.86
22.86 está entre 18.5 y 25 → "Peso normal" 
"""

peso_del_paciente =float(input("Ingresa tu peso en kg: "))
altura_del_paciente = float(input("Ingresa tu altura en metros: "))

imc = (peso_del_paciente)/(altura_del_paciente*altura_del_paciente)

if imc>30: 
    clasificacion_oms = "Riesgo cardiovascular Alto"
elif ((imc>25)&(imc<=30)):
    clasificacion_oms ="Riesgo Cardiovascular moderado"
elif ((imc>18.5)&(imc<25)):
    clasificacion_oms ="Peso normal y saludable"
elif imc <18.5 :
    clasificacion_oms = "Riesgo de desnutricion"

print(f"tu indice de masa corporal es {imc}, tienes un {clasificacion_oms}")
