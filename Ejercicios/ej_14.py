# Ejercicio 14
# Listas
# Objetivo => Guardar múltiples valores
# Enunciado => guarda 5 números en una lista y muestra la suma total
numeros = []
for i in range (5):
    valor = int (input(f"Ingresa el {i+1} número: "))
    numeros.append(valor)
    print("<-------------------------------------->")

print("Suma total: ",sum(numeros))