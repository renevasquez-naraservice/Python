# Funciones
# Ejercicio => Función para calcular el área de un cuadrado, un círculo y un triángulo. La función debe recibir el tipo de figura y las dimensiones necesarias para calcular el área.
import math
# Forma más sencilla 

def calcular_area_cuadrado(lado):
    return lado ** 2    #Se puede usar el operador ** para calcular la potencia, en este caso, el lado al cuadrado para obtener el área del cuadrado.

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Solicitar al usuario el tipo de figura y las dimensiones necesarias
print("\n Parte 1 ----------------------------------------------------------------------- \n")

figura = input("Ingrese el tipo de figura (cuadrado, circulo, triangulo): ")
if figura == "cuadrado":
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = calcular_area_cuadrado(lado)  
    print(f"El área del cuadrado es: {area}")   
elif figura == "circulo":
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area}")    
elif figura == "triangulo":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area}")
else:    print("Figura no reconocida")

# Forma más Completa y ordenada con el uso de funciones y argumentos variables (*args)
def calcular_area(figura, *dimensiones): # *args permite recibir un número variable de argumentos, lo que es útil para manejar diferentes tipos de figuras con diferentes dimensiones.
    if figura == "cuadrado":
        lado = dimensiones[0]
        return lado ** 2
    elif figura == "circulo":
        radio = dimensiones[0]
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base = dimensiones[0]
        altura = dimensiones[1]
        return (base * altura) / 2
    else:
        return "Figura no reconocida"
    
# Solicitar al usuario el tipo de figura y las dimensiones necesarias

print("\n Parte 2 ----------------------------------------------------------------------- \n")
figura = input("Ingrese el tipo de figura (cuadrado, circulo, triangulo): ")
if figura == "cuadrado":
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = calcular_area(figura, lado)  
    print(f"El área del cuadrado es: {area}")
elif figura == "circulo":
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area(figura, radio)
    print(f"El área del círculo es: {area}")
elif figura == "triangulo":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = calcular_area(figura, base, altura)
    print(f"El área del triángulo es: {area}")
else:
    print("Figura no reconocida")