# Ejercicio de Funciones en Python
# Enunciado ==> Función que determine si un número es par o impar. La función debe recibir un número como argumento y devolver "par" o "impar" según corresponda.
def determinar_paridad (numero):
    if numero % 2 == 0: # El operador % (módulo) se utiliza para obtener el resto de la división entre el número y 2. Si el resultado es 0, significa que el número es divisible por 2 y, por lo tanto, es par.
        return "par"
    else:
        return "impar"
    
# Solicitar al usuario un número y mostrar si es par o impar
numero = int(input("Ingrese un número para determinar si es par o impar: "))
resultado = determinar_paridad(numero)
print(f"El número {numero} es {resultado}.")    
