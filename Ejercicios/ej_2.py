# Ejercicio de Condicionales en Python
# Los condicionales son una parte fundamental de la programación, ya que permiten tomar decisiones basadas en ciertas condiciones. A continuación, se presentan algunos ejercicios para practicar el uso de condicionales en Python.
# Objetivo => Practicar el uso de if elif else
# Enunciado => Pide al usuario su edad y determine si es menor de edad, adulto o adulto mayor.
edad = int (input("Ingrese su edad Estimado Usuario: "))
if edad < 0 : 
    print("Usted aún no nace o ingresó una edad inválida")
elif edad < 18 :
    print ("Usted es menor de edad")
elif edad >= 18 and edad < 65 :
    print ("Usted es adulto")
elif edad >= 65 and edad < 120 :
    print ("Usted es adulto mayor")
else: 
    print("Usted es un ser INMORTAL o ha ingresado una edad inválida :)")

# Otra manera de usar los operadores lógicos es con el operador or, en este caso se puede escribir el código de la siguiente manera:
if edad < 0 or edad >= 120 : 
    print("\n ==> Usted ingresó una edad inválida")
# Aqui usamos not para referirnos a la condición contraria, es decir, si la edad no es mayor a 0, entonces se considera inválida.
if not edad > 0:
    print("\n ==> Usted ingresó una edad inválida Negativa")