# Ejercicio 16
# Funciones con Retorno
# Objetivo => Usar 'return'
# Enunciado => Crea una función que calcule el promedio de 3 números
def promedio (a,b,c):
    return (a+b+c)/3

def otro_promedio(lista):
    return (sum(lista))/len(lista)

print(f"Promedio 1: {promedio(1,1,2)}")
print(f"Promedio 2 (lista): {otro_promedio([2,3,4])}")
print("\n --------------------------------------------------------")

# --------------------------------------------------------------------------
# Ejemplo un poco más avanzado pidiendolo al usuario 
valores=[]
for i in range (1,10,2): # range (empieza en, hasta - 1, de cuanto en cuanto) => (1,10,2)
    valores.append(int(input(f"Ingrese el {i} valor entero: ")))
print("El promedio es => ",otro_promedio(valores))