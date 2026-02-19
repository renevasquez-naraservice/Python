# Ejercicio 11
# Condicional Múltiple
# Objetivo => Usar Elif
# Enunciado => Pide al usuario una calificación (0-100) y muestra
# =>Excelente (90 - 100)
# =>Bueno (70 - 89)
# =>Regular (50 - 69)
# =>Reprobado (<50)

nota = int(input("Ingrese su Calificación entera: "))
if nota >=90 and nota <=100:
    print("Excelente")
elif nota >=70:
    print("Bueno")
elif nota >=50:
    print("Regular")
else: 
    print("Reprobado")