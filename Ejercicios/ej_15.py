# Ejercicio 15
# Funciones Básicas
# Objetivo => Crear Funciones
# Enunciado => Crea una función que salude a la persona
def saludar(nombre,**info):
    print(f"Buenos días estimado usuario: {nombre}")
    print(f"Cargo: {info['cargo']}")
    print(f"Salario: {info['salario']}")

saludar("Rene",cargo="Técnico Programador",salario=6500.0)

