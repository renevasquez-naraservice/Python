#Programación Orientada a Objetos (POO) con Python

class Persona: # Define la clase "Persona" que presenta un modelo con atributos y métodos
    def __init__(self, nombre, edad):  # Método especial (CONSTRUCTOR DE CLASE) con atributos de instancia permitiendo que cada instancia teng sus propios valores de nombre y edad
        # self => "Hace referencia al propio objeto" 
        # nombre => "Valor de nombre de la instancia" 
        # edad => "Valor de edad" 
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self): # Método saludar define un comportamiento de la clase usando los atributos para mostrar un mensaje personalizado
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

# ------------------------------------------------------------
# Instanciación de OBJETO PERSONA
p1 = Persona("Carlos", 25)
p1.saludar()

p2 = Persona("Alejandro", 35)
p2.saludar()
